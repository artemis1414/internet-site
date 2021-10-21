from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    phone = models.DecimalField(max_digits=11, decimal_places=0, default=88888888888, help_text='Номер телефона')
