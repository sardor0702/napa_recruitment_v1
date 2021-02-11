from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='main_home'),
    path('accounts/login/', views.login, name='main_login'),
]