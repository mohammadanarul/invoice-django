from io import BytesIO

from xhtml2pdf import pisa

from django.http import HttpResponse
from django.template.loader import get_template

__author__ = "Mohammad Anarul Islam"


def generate_pdf(template_src, context_dict=None):

    if context_dict is None:
        context_dict = {}
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    return (
        None
        if pdf.err
        else HttpResponse(result.getvalue(), content_type="application/pdf")
    )
