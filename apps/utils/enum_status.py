from enum import IntEnum, Enum


class ServiceEnum(IntEnum):
    CLIPPING_PATH = 1
    BACKGROUND_REMOVAL = 2
    DROP_SHADOW = 3
    GHOST_MANNEQUIN = 4
    PHOTO_RETOUCHING = 5
    IMAGE_MASKING = 6
    COLOR_CORRECTION = 7
    PRODUCT_PHOTO = 8

    @classmethod
    def get_service(cls):
        return [(key.value, key.name) for key in cls]


class OrderStatus(IntEnum):
    PENDING = 1
    ACCEPTED = 2
    COMPLETED = 3

    @classmethod
    def get_order_status(cls):
        return [(key.value, key.name) for key in cls]


class InvoiceStatus(Enum):
    PAID = "Paid"
    DUE = "Due"

    @classmethod
    def get_invoice_status(cls):
        return [(key.value, key.name) for key in cls]
