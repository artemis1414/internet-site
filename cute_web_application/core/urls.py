from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sign_in, name='core'),
    path('signup/', views.sign_up, name='sign_up')
]