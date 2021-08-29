from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('<int:product_id>/', views.detail, name='detail'),
]