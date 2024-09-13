from django.urls import path

from .views import *

app_name = 's_profile'

urlpatterns = [
    path('ver/', verif, name='verif'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),
]
