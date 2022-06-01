import markdown
from django.conf import settings
from django.template import Template, RequestContext
from django.views.generic import TemplateView


class MarkdownFileView(TemplateView):
    template_name = "report_base.html"
    markdown_file = None

    def markdown_content(self):
        path = f"{settings.PROJECT_ROOT}/{self.markdown_file}"
        print(path)
        return open(path).read()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        template = Template(self.markdown_content())
        rendered_template = template.render(RequestContext(self.request))
        md = markdown.Markdown(extensions=settings.REPORT_MARKDOWN_EXTENSIONS)
        html = md.convert(rendered_template)
        context["html_content"] = html
        context["toc"] = md.toc
        context["page_title"] = md.toc_tokens[0]["name"]
        return context
