from datetime import date
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, View
from apps.utils.render_to_pdf import generate_pdf
from apps.invoice.models import Invoice


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["invoices"] = Invoice.objects.all()
        return context


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = "invoice/detail.html"


class InvoicePDFDownload(View):
    def get(self, **kwargs):
        try:
            print("kwargs", kwargs["pk"])
            invoice = Invoice.objects.get(pk=kwargs["pk"])
            print(invoice)
            pdf = generate_pdf("invoice/pdf.html", {"object": invoice})
            response = HttpResponse(pdf, content_type="application/pdf")
            filename = f"Damage-Data-{date.today()}.pdf"
            content = f"attachment; filename={filename}"
            response["Content-Disposition"] = content
            return response
        except Exception as e:
            print(e)
