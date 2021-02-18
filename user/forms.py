from django import forms
from napa_recruitment.validators import PhoneValidator
from django.core.validators import MinLengthValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from user.models import User


# class RegistrationForm(forms.ModelForm):
#     phone = forms.CharField(max_length=14, required=True, validators=[PhoneValidator()], placeholder="998991234567")
#     password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True,
#                                validators=[MinLengthValidator(6)])
#     confirm = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True,
#                               validators=[MinLengthValidator(6)])
#
#     class Meta:
#         model = User
#         fields = ('phone', 'username', 'password', 'confirm')


class LoginForm(forms.ModelForm):

    username = forms.CharField(max_length=20, required=True,  validators=[UnicodeUsernameValidator()])
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True,
                               validators=[MinLengthValidator(6)])

    class Meta:
        model = User
        fields = ('username', 'password')


class RegistrationForm(forms.Form):
    phone = forms.CharField(max_length=14, required=True,
                            validators=[PhoneValidator()])
    username = forms.CharField(max_length=20, required=True,
                               validators=[UnicodeUsernameValidator()])
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True,
                               validators=[MinLengthValidator(6)])
    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True,
                               validators=[MinLengthValidator(6)])

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data.get('username')).exists():
            raise ValidationError("Ushbu nickname band")

        return self.cleaned_data["username"]

    def clean_phone(self):
        if User.objects.filter(phone=self.cleaned_data.get('phone')).exists():
            raise ValidationError("Ushbu telefon raqam band")

        return self.cleaned_data["phone"]

    def clean_confirm(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm']:
                raise ValidationError("Parollar bir xil emas")

        return self.cleaned_data['confirm']
