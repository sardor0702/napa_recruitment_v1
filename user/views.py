from rest_framework.views import APIView
from .serializers import UserSerializer, RegistrationSerializer
# from napa_recruitment.responses import ResponseSuccess, ResponseFile
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegistrationForm, LoginForm, EditForm, ForgotPassword
from .models import User
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.views.generic import CreateView


class UserRegistration(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = "Sign up"

    def get(self, request):
        form = RegistrationForm()
        return render(request, "main/sign_up.html", {
            'form': form
        })

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            del data['confirm']
            user = User(**data)

            user.set_password(user.password)
            user.save()
            return redirect('user:login')
        return render(request, "main/sign_up.html", {
            'form': form
        })


def user_login(request):
    request.title = "Авторизоваться"

    form = LoginForm()
    if request.POST:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                messages.success(request, "Добро пожаловать !!!  {}".format(user.username))
                return redirect('user:personal_account')

            form.add_error('password', "Имя пользователя и пароль неверны !")
        return render(request, 'main/sign_in.html', {
                'form': form,
        })
    return render(request, 'main/sign_in.html', {
        'form': form
    })


@login_required
def login_checkin(request):
    request.title = "Персональный аккаунт"
    form = LoginForm(data=request.user)  #user ma'lumotlarini jo'natvoman
    return render(request, 'main/personal_account.html', {
        'form': form
    })


@login_required
def user_logout(request):
    logout(request)
    return redirect("main:main_home")


@require_GET
@login_required
def user_info(request, id):
    request.title = "Личный кабинет"
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return redirect('personal_account')

    return render(request, "main/personal_account_changing_info.html",
                  {
                      'form': EditForm(instance=request.user),
                      'user': user
                  })


@require_POST
@login_required
def user_info_post(request):
    form = EditForm(data=request.POST, instance=request.user, files=request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Сохранено")
        return redirect('user:personal_account')

    return render(request, "main/personal_account_changing_info.html", {
        'form': form
    })


def forgot_password(request):
    request.title = "Забыли пароль"
    form = ForgotPassword()
    return render(request, "main/forgot_password.html", {
        'form': form
    })


@require_GET
def get_code(request):
    pass


@require_POST
def post_code(request):
    pass