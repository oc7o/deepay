from django import forms
from .models import ProductInventory, Media


class AddToBasketForm(forms.Form):
    qty = forms.IntegerField(min_value=1, max_value=100)


class ProductInventoryCreateForm(forms.ModelForm):
    units = forms.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = ProductInventory
        fields = [
            "product_type",
            "describing_keyword",
            "is_default",
            "store_price",
        ]


class ProductInventoryUpdateForm(forms.ModelForm):
    units = forms.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = ProductInventory
        fields = [
            "product_type",
            "describing_keyword",
            "is_default",
            "store_price",
            "is_active",
        ]
