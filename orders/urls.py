from django.urls import path

from .views import *

app_name = 'orders'

urlpatterns = [
    path('', orders_list, name='orders_list'),
    path('order/', order_detail, name='order_detail'),
    path('create/', order_create, name='order_create'),
    path('success/', success, name='success'),
]
