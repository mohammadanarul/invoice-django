import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStamp
from apps.utils.enum_status import ServiceEnum, OrderStatus


class Order(TimeStamp):
    order_id = models.CharField(max_length=15, blank=True)
    service = models.IntegerField(
        choices=ServiceEnum.get_service(), default=ServiceEnum.CLIPPING_PATH
    )
    quantity = models.PositiveBigIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(200)]
    )
    url = models.URLField(_("file url"), blank=True)
    return_image_format = models.CharField(_("return image format"), max_length=10)
    description = models.TextField()
    status = models.IntegerField(
        choices=OrderStatus.get_order_status(), default=OrderStatus.PENDING
    )

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = str(uuid.uuid4()).replace("-", "")[:15]
            super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.order_id
