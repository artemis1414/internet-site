from .models import User
from django import forms

class SignUpForm(forms.Form):
    login = forms.CharField(label='Ваш логин')
    password = forms.CharField(label="Пароль")
    phone = forms.DecimalField(label="Телефон", max_digits=11, decimal_places=0)
    email = forms.EmailField(label="Email")
