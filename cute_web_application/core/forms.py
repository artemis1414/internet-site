from .models import User
from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(label='Ваш логин')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    password = forms.CharField(label="Пароль")
    phone = forms.DecimalField(label="Телефон", max_digits=11, decimal_places=0, required=False)
    email = forms.EmailField(label="Email")

class UpdateProfile(forms.Form):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    phone = forms.DecimalField(label="Телефон", max_digits=11, decimal_places=0, required=False)
