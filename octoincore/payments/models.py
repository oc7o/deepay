from django.db import models

# from picklefield.fields import PickledObjectField

from octoincore.inventory.models import ProductInventory


# class BTCPayClientStore(models.Model):
#     client = PickledObjectField()


# class BTCPayBinding(models.Model):
#     token = models.CharField(max_length=255)
#     btcpay_instance: str = models.CharField(max_length=2023)
#     default_store_id: str = models.CharField(max_length=255)
#     default_currency: str = models.CharField(max_length=255)


class Order(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)


class OrderProductInventory(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_product_inventories"
    )
    product_inventory = models.ForeignKey(
        ProductInventory, on_delete=models.PROTECT, related_name="orders"
    )
    quantity = models.IntegerField()


class OrderInvoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="invoices")
    invoice_id = models.CharField(max_length=255)
    invoice_url = models.URLField()
    # status = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # created_at = models.DateTimeField()
    # expired_at = models.DateTimeField()
    # currency = models.CharField(max_length=255)
    # date = models.DateTimeField()
