from django import template
from django.utils.safestring import mark_safe

import markdown

register = template.Library()


@register.filter(name="markdown")
def markdown_filter(text):
    return mark_safe(markdown.markdown(text))


markdown_filter.is_safe = True


@register.tag(name="markdown")
def markdown_tag(parser, token):
    nodelist = parser.parse(("endmarkdown",))
    bits = token.split_contents()
    if len(bits) == 1:
        style = "default"
    elif len(bits) == 2:
        style = bits[1]
    else:
        raise template.TemplateSyntaxError(
            "`markdown` tag requires exactly " "zero or one arguments"
        )
    parser.delete_first_token()  # consume '{% endmarkdown %}'
    return MarkdownNode(style, nodelist)


class MarkdownNode(template.Node):
    def __init__(self, style, nodelist):
        self.style = style
        self.nodelist = nodelist

    def render(self, context):
        value = self.nodelist.render(context)
        return mark_safe(markdown.markdown(value, self.style))
