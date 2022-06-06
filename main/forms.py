from django import forms
from django_select2.forms import Select2Widget, Select2MultipleWidget
from main.models import FilterValues


class SearchForm(forms.Form):
    query = forms.ModelChoiceField(
        widget=Select2MultipleWidget(attrs={'style': 'border-radius: 20px;'}),
        queryset=FilterValues.objects.all(),
        initial=''
    )
