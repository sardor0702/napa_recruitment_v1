from django import forms
# from django.contrib.auth.models import User
from user.models import User
from django.contrib.auth.hashers import make_password


class RegisterForm(forms.ModelForm):
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('phone', 'username', 'password')


class LoginForms(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    # class Meta:
    #     model = User
    #     fields = ('username', 'password')


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = [
#             'company_name',
#             'full_name',
#             'activity_company',
#             'phone',
#             'mobil_phone',
#             'email'
#         ]


