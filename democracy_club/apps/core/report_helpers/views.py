import markdown_deux
from django.conf import settings
from django.template import Template, RequestContext
from django.template.loader import render_to_string
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

        markdown_doc = markdown_deux.markdown(
            rendered_template, style="default"
        )
        context["toc"] = markdown_doc.toc_html


        context["html_content"] = markdown_doc

        return context
