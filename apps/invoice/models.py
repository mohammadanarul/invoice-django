from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from apps.common.models import TimeStamp
from apps.utils.enum_status import ServiceEnum, InvoiceStatus


class Invoice(TimeStamp):
    invoice_id = models.CharField(max_length=15)
    client_name = models.CharField(max_length=255)
    client_phone_number = models.CharField(max_length=255)
    client_address = models.CharField(max_length=255)

    def __str__(self):
        return self.invoice_id


class InvoiceItem(TimeStamp):
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name="invoice_items"
    )
    order_id = models.CharField(max_length=8)
    order_service = models.IntegerField(
        choices=ServiceEnum.get_service(), default=ServiceEnum.CLIPPING_PATH
    )
    order_quantity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(500)]
    )
    status = models.IntegerField(
        choices=InvoiceStatus.get_invoice_status(), default=InvoiceStatus.DUE
    )

    def __str__(self):
        return f"{self.order_id}->{self.invoice}"
