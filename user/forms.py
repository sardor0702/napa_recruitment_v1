from django import forms
from napa_recruitment.validators import PhoneValidator
from django.core.validators import MinLengthValidator, EmailValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from user.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, label=False)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True,
                               validators=[MinLengthValidator(6)], label=False)


class RegistrationForm(forms.Form):
    phone = forms.CharField(max_length=14, required=True, validators=[PhoneValidator()],
                            widget=forms.TextInput(attrs={'placeholder': '998971234567'}), label=False)
    username = forms.CharField(max_length=20, required=True,
                               validators=[UnicodeUsernameValidator()], label=False)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True,
                               validators=[MinLengthValidator(6)], label=False)
    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True,
                              validators=[MinLengthValidator(6)], label=False)

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
    avatar = forms.ImageField(widget=forms.FileInput(attrs=({"name": "inpFile", "id": "inpFile"})), label=False,
                              required=False)
    company_name = forms.CharField(max_length=50, label=False,
                                   widget=forms.TextInput(attrs=({"class": "rounded-15"})), required=True)
    first_name = forms.CharField(max_length=50, label=False,
                                 widget=forms.TextInput(attrs=({"class": "rounded-15"})), required=True)
    last_name = forms.CharField(max_length=50, label=False,
                                widget=forms.TextInput(attrs=({"class": "rounded-15"})), required=True)
    activity_company = forms.CharField(max_length=150, label=False,
                                       widget=forms.TextInput(attrs=({"class": "rounded-15"})), required=False)
    phone = forms.CharField(max_length=16, label=False,
                            widget=forms.TextInput(attrs=({"class": "rounded-15"})),
                            validators=[PhoneValidator()],
                            required=True)
    mobil_phone = forms.CharField(max_length=16, label=False,
                                  widget=forms.TextInput(attrs=({"class": "rounded-15"})),
                                  required=False)
    email = forms.EmailField(max_length=100, label=False, widget=forms.EmailInput(attrs=({"class": "rounded-15"})) )

    class Meta:
        model = User
        fields = [
            'avatar',
            'company_name',
            'first_name',
            'last_name',
            'activity_company',
            'phone',
            'mobil_phone',
            'email',
        ]


class ForgotPassword(forms.Form):
    phone = forms.CharField(max_length=16, label=False,
                            widget=forms.TextInput(attrs=({"class": "rounded-15", 'placeholder': '998971234567'})), validators=[PhoneValidator()],
                            required=True)


class ChangePassword(forms.Form):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs=({"class": "rounded-15"})),
                                   required=True, validators=[MinLengthValidator(6)], label=False)
    new_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs=({"class": "rounded-15"})),
                                   required=True, validators=[MinLengthValidator(6)], label=False)
    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs=({"class": "rounded-15"})),
                              required=True, validators=[MinLengthValidator(6)], label=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ChangePassword, self).__init__(*args, **kwargs)

    def clean_confirm(self):
        if self.cleaned_data['new_password'] != self.cleaned_data['confirm']:
            raise ValidationError("Parollar bir xil emas")

        return self.cleaned_data['confirm']

    def clean_old_password(self):
        password = self.cleaned_data['old_password']

        if not self.user.check_password(password):
            raise ValidationError("Old password didn't match")

