import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from apps.common.models import TimeStamp
from apps.utils.enum_status import ServiceEnum, InvoiceStatus


class Invoice(TimeStamp):
    invoice_id = models.CharField(max_length=15, blank=True)
    client_name = models.CharField(max_length=255)
    client_phone_number = models.CharField(max_length=255)
    client_address = models.CharField(max_length=255)
    status = models.CharField(
        choices=InvoiceStatus.get_invoice_status(),
        default=InvoiceStatus.DUE,
        max_length=4,
    )

    def save(self, *args, **kwargs):
        if not self.invoice_id:
            self.invoice_id = "INV" + str(uuid.uuid4()).replace("-", "")[:12]
            super(Invoice, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("invoice-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.invoice_id


class InvoiceItem(TimeStamp):
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name="invoice_items"
    )
    order_id = models.CharField(max_length=15)
    order_service = models.IntegerField(
        choices=ServiceEnum.get_service(), default=ServiceEnum.CLIPPING_PATH
    )
    order_quantity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(500)]
    )

    def __str__(self):
        return f"{self.order_id}->{self.invoice}"
