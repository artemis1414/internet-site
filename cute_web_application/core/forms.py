from .models import User
from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(label='Ваш логин')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password_1 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput)
    phone = forms.DecimalField(label="Телефон", max_digits=11, decimal_places=0)
    email = forms.EmailField(label="Email")

class UpdateProfile(forms.Form):
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)
    phone = forms.DecimalField(label="Телефон", max_digits=11, decimal_places=0, required=False)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput, required=False)
    password_1 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput, required=False)
