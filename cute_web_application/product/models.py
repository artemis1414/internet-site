from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(default='name', help_text='Наименование товара')
    description = models.TextField(default='description', help_text='Описание товара')
    price = models.IntegerField(default=0, help_text='Цена товара')
    value = models.IntegerField(default=0, help_text='Количество товара')
    category = models.TextField(default='category', help_text='Тип товара')
    material = models.TextField(default='material', help_text='Материал товара')
    color = models.TextField(default='color', help_text='Цвет товара')
    manufacturer = models.TextField(default='manufacturer', help_text='Производитель товара')
    link = models.TextField(default='.', help_text='Ссылка на фото товара')
    update_on = models.DateTimeField(auto_now=True, help_text='Время обновления записи')
    created_on = models.DateTimeField(auto_now_add=True, help_text='Время создания записи')
    size_36_value = models.IntegerField(default=0, help_text='Количество товара 36 размера')
    size_37_value = models.IntegerField(default=0, help_text='Количество товара 37 размера')
    size_38_value = models.IntegerField(default=0, help_text='Количество товара 38 размера')
    size_39_value = models.IntegerField(default=0, help_text='Количество товара 39 размера')
    size_40_value = models.IntegerField(default=0, help_text='Количество товара 40 размера')

    def __str__(self):
        return '{}'.format(self.name)
