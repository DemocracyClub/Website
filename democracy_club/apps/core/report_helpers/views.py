import markdown
from django.conf import settings
from django.template import RequestContext, Template
from django.views.generic import TemplateView


class MarkdownFileView(TemplateView):
    template_name = "report_base.html"
    markdown_file = None

    def markdown_content(self):
        path = f"{settings.PROJECT_ROOT}/{self.markdown_file}"

        with open(path) as f:
            return f.read()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        template = Template(self.markdown_content())
        rendered_template = template.render(RequestContext(self.request))
        self.md = markdown.Markdown(
            extensions=settings.REPORT_MARKDOWN_EXTENSIONS
        )
        self.html = self.md.convert(rendered_template)
        context["html_content"] = self.html
        context["toc"] = self.md.toc
        context["page_title"] = self.md.toc_tokens[0]["name"]
        context["report_metadata"] = self.md.Meta
        context["report_hero_image"] = self.report_hero_image()
        return context

    def report_hero_image(self):
        hero_image = self.md.Meta.get("hero_image", None)
        if hero_image:
            return hero_image[0]
        return None
