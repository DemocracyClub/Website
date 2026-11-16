import hashlib

from django.http import Http404
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.http import condition
from django.views.generic import DetailView, ListView
from hermes.models import Post, Tag


def latest_post(request, *args, **kwargs):
    return Post.objects.latest().modified_on


def get_etag(request, *args, **kwargs):
    post_modified_on = str(latest_post(request, *args, **kwargs))
    return hashlib.md5(
        "-".join(("blog", post_modified_on)).encode("utf-8")
    ).hexdigest()


@method_decorator(
    condition(last_modified_func=latest_post, etag_func=get_etag), name="get"
)
class PostListView(ListView):
    """Base Post List View."""

    context_object_name = "posts"
    model = Post
    template_name = "hermes/post_list.html"

    def get(self, request, *args, **kwargs):
        # Old-style /blog/?tag=Foo links go to the tag's own page
        tag = Tag.objects.resolve(request.GET.get("tag"))
        if tag:
            return redirect(tag, permanent=True)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return (
            self.model.objects.published()
            .prefetch_related("author", "tags")
            .defer("body", "hero_alt_text")
        )

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        # Every tag with a published post, so the filter is the same
        # on every page rather than depending on what's being listed
        context["all_tags"] = Tag.objects.filter(
            posts__is_published=True
        ).distinct()
        return context


class TagPostListView(PostListView):
    """Displays posts from a specific Tag"""

    def get(self, request, *args, **kwargs):
        self.tag = Tag.objects.resolve(self.kwargs["tag"])
        if self.tag is None:
            raise Http404("No such tag")
        if self.tag.slug != self.kwargs["tag"]:
            # A renamed tag, or an old mixed-case URL such as
            # /blog/tag/WhoCanIVoteFor/
            return redirect(self.tag, permanent=True)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.for_tag(self.tag).prefetch_related(
            "author", "tags"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag
        return context


class CategoryPostListView(PostListView):
    """Displays posts from a specific Category"""

    def get_queryset(self):
        category_slug = self.kwargs.get("slug", "")
        return self.model.objects.in_category(category_slug)


class ArchivePostListView(PostListView):
    """Displays posts from a specific Year/Month/Day"""

    def get_queryset(self):
        year = self.kwargs.get("year", None)
        month = self.kwargs.get("month", None)
        day = self.kwargs.get("day", None)

        return self.model.objects.created_on(year=year, month=month, day=day)


class AuthorPostListView(PostListView):
    """Displays posts from a specific Author"""

    def get_queryset(self):
        author = self.kwargs.get("author", "")
        return self.model.objects.by(author)


class PostDetail(DetailView):
    context_object_name = "post"
    model = Post
    template_name = "hermes/post_detail.html"
