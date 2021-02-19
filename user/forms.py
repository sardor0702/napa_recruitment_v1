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
    phone = forms.CharField(max_length=14, required=True,
                            validators=[PhoneValidator()], widget=forms.TextInput(attrs={'placeholder': '998971234567'}))
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
    # company_name = forms.CharField(max_length=50, label="Наименование компании", help_text="50 ta harifdan ko'p bo'lmaslin!!!")
    # first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    #     "style": "background: red"
    # }))
    avatar = forms.ImageField(widget=forms.FileInput(attrs=({"name": "inpFile", "id": "inpFile"})), label=False,
                              validators=[])
    company_name = forms.CharField(max_length=50, label=False,
                                   widget=forms.TextInput(attrs=({"class": "rounded-15"})), required=True)
    first_name = forms.CharField(max_length=50, label=False,
                                 widget=forms.TextInput(attrs=({"class": "rounded-15"})), required=True)
    last_name = forms.CharField(max_length=50, label=False,
                                widget=forms.TextInput(attrs=({"class": "rounded-15"})), required=True)
    activity_company = forms.CharField(max_length=150, label=False,
                                       widget=forms.TextInput(attrs=({"class": "rounded-15"})))
    phone = forms.CharField(max_length=16, label=False,
                            widget=forms.TextInput(attrs=({"class": "rounded-15"})), validators=[PhoneValidator()],
                            required=True)
    mobil_phone = forms.CharField(max_length=16, label=False,
                                  widget=forms.TextInput(attrs=({"class": "rounded-15"})), validators=[PhoneValidator()])
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

    # company_name = forms.CharField(max_length=80, required=True)
    # first_name = forms.CharField(max_length=30, required=True)
    # last_name = forms.CharField(max_length=40, required=True)
    # activity_company = forms.CharField(max_length=80)
    # phone = forms.CharField(max_length=16, validators=[PhoneValidator()], required=True)
    # mobil_phone = forms.CharField(max_length=16, validators=[PhoneValidator()])
    # email = forms.EmailField(max_length=100, validators=[EmailValidator()])
