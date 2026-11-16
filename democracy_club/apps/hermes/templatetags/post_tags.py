from django import template
from hermes.models import Post, Tag

register = template.Library()


def posts_for_tag(tag_slug, hide_header=False):
    tag = Tag.objects.resolve(tag_slug)
    posts = Post.objects.for_tag(tag).published()[:4] if tag else []
    return {
        "posts": posts,
        "tag": tag,
        "hide_header": hide_header,
    }


register.inclusion_tag("hermes/posts_for_tag.html")(posts_for_tag)
