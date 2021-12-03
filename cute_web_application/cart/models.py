from django.db import models
from core.models import User
from product.models import Product
# Create your models here.


class CartItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, to_field='id')
    products = models.TextField(default='Пусто', help_text='Корзина')

class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, to_field='id')
    name_and_phone = models.TextField(help_text='Имя и телефон заказчика', null=True)
    structure = models.TextField(default='Пусто', help_text='Состав заказа')
    cost = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, help_text='Стоимость заказа')
    address = models.CharField(max_length=300, null=True, help_text='Адрес доставки')
    created_on = models.DateTimeField(auto_now_add=True, help_text='Время создания записи')


