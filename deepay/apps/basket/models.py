from django.db import models

from deepay.models import DefaultModel


class BasketObject(DefaultModel):
    """
    BasketObject model
    """

    basket = models.ForeignKey(
        "basket.Basket",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="basket_objects",
    )
    inventory = models.ForeignKey(
        "inventory.ProductInventory",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="baskets",
    )
    qty = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.inventory.product.name} - {self.qty}"

    def __unicode__(self):
        return self.basket_object_id

    class Meta:
        db_table = "basket_object"
        verbose_name = "BasketObject"
        verbose_name_plural = "BasketObjects"


class Basket(DefaultModel):
    """
    Basket model
    """

    locked = models.BooleanField(default=False)

    def add(self, inventory, qty):
        if self.locked:
            raise Exception("Basket is locked")

        basket_object, created = BasketObject.objects.get_or_create(
            basket=self, inventory=inventory
        )
        if not created:
            basket_object.qty += qty
        else:
            basket_object.qty = qty
        basket_object.save()

    def remove(self, inventory):
        if self.locked:
            raise Exception("Basket is locked")

        basket_object = BasketObject.objects.get(basket=self, inventory=inventory)
        basket_object.delete()

    @property
    def total_price(self):
        total = 0
        for basket_object in self.basket_objects.all():
            total += basket_object.inventory.store_price * basket_object.qty
        return total

    @property
    def total_qty(self):
        total = 0
        for basket_object in self.basket_objects.all():
            total += basket_object.qty
        return total

    def __unicode__(self):
        return self.basket_id

    class Meta:
        db_table = "basket"
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"
