from django import forms
from django.core.validators import MinLengthValidator
# from django.contrib.auth.models import User
from django_select2.forms import Select2Widget, Select2MultipleWidget

from main.models import FilterValues
from user.models import User
from django.contrib.auth.hashers import make_password


class SearchForm(forms.Form):
    query = forms.ModelChoiceField(
        widget=Select2MultipleWidget(attrs={'style': 'border-radius: 20px;'}),
        queryset=FilterValues.objects.all(),
        initial=''
    )
