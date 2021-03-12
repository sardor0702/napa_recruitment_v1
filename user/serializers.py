from rest_framework import serializers
from rest_framework.validators import *
from .models import User
from django.core.validators import MinLengthValidator, RegexValidator
from napa_recruitment.validators import PhoneValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.text import gettext_lazy as _
from django.contrib.auth.models import Group


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=50)

    def to_internal_value(self, data):
        data["username"] = PhoneValidator.clean(data.get("username"))
        return super(LoginSerializer, self).to_internal_value(data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'perms', 'card']


class RegistrationSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        data["phone"] = PhoneValidator.clean(data.get("phone"))
        return super(RegistrationSerializer, self).to_internal_value(data)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']
        extra_kwargs = {
            'username': {
                'validators': [PhoneValidator(), UniqueValidator(
                    queryset=User.objects.all(),
                    message=_("Ushbu telefon raqam allaqachon tizimdan ro'yxatdan o'tgan")
                )],
                # 'unique': True,
                'max_length': 12
            },
            'first_name': {
                'required': True,
                'validators': []
            },
            'last_name': {
                'required': True,
                'validators': []
            },
            'password': {
                'validators': [MinLengthValidator(6)]
            }
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name')


# class RegistrationSerializer(serializers.Serializer):
#
#     phone = serializers.CharField(max_length=15, validators=[
#         PhoneValidator()
#     ], required=True)
#
#
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#
#     def validate_first_name(self, value):
#         raise ValueError("nice")
