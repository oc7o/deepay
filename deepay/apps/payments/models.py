from django.db import models

from deepay.apps.basket.models import Basket
from deepay.models import DefaultModel


class Order(DefaultModel):
    # TODO: add owner
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    status = models.CharField(
        max_length=255,
        default="new",
        choices=[
            ("unknown", "unknown"),
            ("new", "new"),
            ("paid", "paid"),
            ("shipped", "shipped"),
            ("canceled", "canceled"),
            ("done", "done"),
            ("objected", "objected"),
        ],
    )

    basket = models.OneToOneField(
        Basket, on_delete=models.CASCADE, related_name="order"
    )

    def __str__(self):
        return f"{self.status} - {self.web_id}"


class OrderInvoice(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name="invoice"
    )
    invoice_id = models.CharField(max_length=255)
    invoice_url = models.URLField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
