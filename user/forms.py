from django import forms
from napa_recruitment.validators import PhoneValidator
from django.core.validators import MinLengthValidator, EmailValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from user.models import User


class LoginForm(forms.Form):

    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True,
                               validators=[MinLengthValidator(6)])


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


class EditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'company_name',
            'first_name',
            'last_name',
            'activity_company',
            'phone',
            'mobil_phone',
            'email',
        ]

    # company_name = forms.CharField(max_length=80, required=True)
    # first_name = forms.CharField(max_length=30, required=True)
    # last_name = forms.CharField(max_length=40, required=True)
    # activity_company = forms.CharField(max_length=80)
    # phone = forms.CharField(max_length=16, validators=[PhoneValidator()], required=True)
    # mobil_phone = forms.CharField(max_length=16, validators=[PhoneValidator()])
    # email = forms.EmailField(max_length=100, validators=[EmailValidator()])
