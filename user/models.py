from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager():
    def create_user(self, **kwargs):
        raise Exception("create user")


    def create_superuser(self, **kwargs):
        raise Exception("create super user")


class User(AbstractUser):
    objects = UserManager()
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=30, help_text="Пожалуйста, укажите ваше имя пользователя", unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=100, help_text="Пожалуйста, укажите свой пароль")
    phone = models.CharField(max_length=16, help_text="Пожалуйста, предоставьте свой телефон")
    mobil_phone = models.CharField(max_length=16)
    avatar = models.ImageField(upload_to='avatars')
    # email = models.EmailField(max_length=100)
    company_name = models.CharField(max_length=255)
    activity_company = models.CharField(max_length=255)
    is_admin = models.SmallIntegerField(default=0)

