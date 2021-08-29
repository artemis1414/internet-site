from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signinsystem, name='core'),
    path('registration/', views.registration, name='registration')
]