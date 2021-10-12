from django.urls import path, include
from . import views

urlpatterns = [
    path('category/', views.product, name='product'),
    path('category/<int:category_id>/item<int:product_id>/', views.detail, name='detail'),
    path('category/<int:category_id>/', views.catalog, name='catalog'),
]