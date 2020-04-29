from django.views.generic.base import TemplateView
from django.template.loader import get_template

import markdown_deux


class ReportView(TemplateView):
    template_name = "report_whos_missing/report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        md = get_template(self.template_name).template.source
        md_with_toc = markdown_deux.markdown(md, "default")
        context["toc"] = md_with_toc.toc_html
        return context
