from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from napa_recruitment.validators import PhoneValidator


class UserManager(BaseUserManager):
    def __create_user(self, phone, password, **kwargs):
        phone = PhoneValidator.clean(phone)
        validator = PhoneValidator()
        validator(phone)

        user = User(**kwargs)
        user.phone = phone
        user.set_password(password)

        user.save()

    def create_user(self, *args, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)

        if kwargs.get('is_staff') or kwargs.get('is_superuser'):
            raise Exception("User is_staff=False va is_superuser=False bo'lishi shart")

        return self.__create_user(*args, **kwargs)

    def create_superuser(self, *args, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if not kwargs.get('is_staff') or not kwargs.get('is_superuser'):
            raise Exception("User is_staff=True va is_superuser=True bo'lishi shart")

        # print(args, kwargs)

        return self.__create_user(*args, **kwargs)

    def get_by_natural_key(self, username):
        return User.objects.get(username=username)


class User(AbstractUser):
    objects = UserManager()
    password = models.CharField(max_length=100, help_text="Пожалуйста, укажите свой пароль")
    phone = models.CharField(max_length=15, unique=True, help_text="Пожалуйста, предоставьте свой телефон")
    mobil_phone = models.CharField(max_length=16)
    avatar = models.ImageField(upload_to='avatars')
    company_name = models.CharField(max_length=255)
    activity_company = models.CharField(max_length=255)

    USERNAME_FIELD = 'phone'
    username_validator = PhoneValidator()

    @property
    def full_name(self):
        return "{} {}".format(self.last_name, self.first_name)


# user = User.objects.all()
# for i in user:
#     i.