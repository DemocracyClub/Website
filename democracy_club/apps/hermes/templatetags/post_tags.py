from django import template
from hermes.models import Post

register = template.Library()


def posts_for_tag(tag, hide_header=False):
    posts = Post.objects.for_tag(tag)[:4]
    return {
        "posts": posts,
        "tag": tag,
        "hide_header": hide_header,
    }


register.inclusion_tag("hermes/posts_for_tag.html")(posts_for_tag)
