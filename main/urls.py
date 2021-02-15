from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='main_home'),
    path('accounts/login/', views.login, name='main_login'),
    path('accounts/personal/', views.login_checkin, name='main_checkin'),
    path('accounts/registration/', views.register, name='main_registration'),
    path('accounts/registration_post/', views.register_post, name="main_registration_post"),
    path('forgot_password/', views.forgot_password, name='forgot_password')
]