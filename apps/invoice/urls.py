from django.urls import path
from apps.invoice import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path(
        "invoice/<pk>/detail/", views.InvoiceDetailView.as_view(), name="invoice-detail"
    ),
    path(
        "invoice/<pk>/pdf/download/",
        views.InvoicePDFDownload.as_view(),
        name="invoice-download",
    ),
]
