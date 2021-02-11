from django.shortcuts import render
from . import views

def home(request):
    return render(request, 'main/home_page.html')

def login(request):
    return render(request, 'main/sign_in.html', {'title': 'Login'})
