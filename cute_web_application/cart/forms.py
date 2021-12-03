from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class AddOrder(forms.Form):
    name = forms.CharField(max_length=120, label='Ваше имя')
    phone = forms.IntegerField(min_value=70000000000, max_value=89999999999, label='Ваш телефон')
    address = forms.CharField(max_length=300, label='Адрес доставки')
