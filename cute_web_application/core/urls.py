from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sign_in, name='core'),
    path('signup/', views.sign_up, name='sign_up'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sell_history/', views.sell_history, name='sell_history'),
    path('sell_history/order_<int:order_id>', views.detail_order, name='detail_order'),
    path('change_profile/', views.update_profile, name='change_profile'),
]
