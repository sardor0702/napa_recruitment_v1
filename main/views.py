from django.shortcuts import render, redirect
from . import views
from .forms import RegisterForm, LoginForms
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    context = {}
    return render(request, 'main/home_page.html', context)


def login(request):
    form = LoginForms()

    if request.method == "POST":
        form = LoginForms(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                dj_login(request, user)
                return redirect('main_checkin')

    context = {
        'form': form,
        'title': 'Login'
    }
    return render(request, 'main/sign_in.html', context=context)


@login_required
def login_checkin(request):
    form = LoginForms(data=request.user)  #user ma'lumotlarini jo'natvoman
    context = {
        'form': form,
        'title': 'Personal account'
    }
    return render(request, 'main/personal_account.html', context=context)


def register(request):
    context = {
        'form': RegisterForm,
        'title': 'Registration'
    }
    return render(request, 'main/sign_up.html', context=context)


def register_post(request):
    form = RegisterForm(request.POST)
    if not form.is_valid():  # formada kevotgan ma'lumot to'g'ri kemas...
        return render(request, 'main/sign_up.html', {'form':form})
    form.save()
    return redirect('main_login')


def forgot_password(request):
    return render(request, 'main/forgot_password.html', {'title': 'Forgot password'})
