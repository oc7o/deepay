from django import forms


class AddToBasketForm(forms.Form):
    qty = forms.IntegerField(min_value=1, max_value=100)
