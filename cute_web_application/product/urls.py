from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('1', views.product1, name='product'),
]