from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.BigAutoField(primary_key=1)
    name = models.TextField(default='name')
    description = models.TextField(default='description')
    price = models.IntegerField(default=0)
    value = models.IntegerField(default=0)
    category = models.TextField(default='category')
    material = models.TextField(default='material')
    color = models.TextField(default='color')
    manufacturer = models.TextField(default='manufacturer')
    link = models.TextField(default='https://static.onlinetrade.ru/img/items/b/1348575_1.jpg')

    def __str__(self):
        return '{}'.format(self.name)
