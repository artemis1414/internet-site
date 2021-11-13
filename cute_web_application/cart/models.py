from django.db import models
from core.models import User
from product.models import Product
# Create your models here.


class CartItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, to_field='id')
    products = models.TextField(default='Пусто', help_text='Корзина')
