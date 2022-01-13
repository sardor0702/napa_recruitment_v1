from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import View
from .forms import RegistrationForm, LoginForm, EditForm, ForgotPassword, ChangePassword, GetCodeForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import update_session_auth_hash
from .serializers import UserSerializer, LoginSerializer, RegistrationSerializer
from rest_framework import permissions
from napa_recruitment.helpers import *
from django.core.exceptions import ValidationError


class UserRegistration(View):
    permission_classes = [~permissions.IsAuthenticated]

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

    def get(self, request):
        form = RegistrationForm()
        context = _("Регистрация")
        return render(request, "main/sign_up.html", {
            'form': form,
            "title": context
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
    request.title = _("Авторизоваться")

    form = LoginForm()
    if request.POST:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
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
    request.title = _("Персональный аккаунт")
    form = LoginForm(data=request.user)  # user ma'lumotlarini jo'natvoman
    return render(request, 'main/personal_account.html', {
        'form': form
    })


@login_required
def user_logout(request):
    logout(request)
    return redirect("user:login")


@require_GET
@login_required
def user_info(request, id):
    request.title = _("Личный кабинет")
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return redirect('personal_account')
    password_form = ChangePassword()
    return render(request, "main/personal_account_changing_info.html",
                  {
                      'form': EditForm(instance=request.user),
                      'user': user,
                      'password_form': password_form
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


@require_POST
@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePassword(request.POST, user=request.user)
        if form.is_valid():
            request.user.set_password(form.cleaned_data['confirm'])
            request.user.save()
            update_session_auth_hash(request, request.user)  # Important!
            messages.success(request, 'Ваш пароль успешно обновлен!')
            return redirect('user:personal_account')
        else:
            messages.error(request, 'Пароль не обновлен.')
    return redirect('user:info', id=request.user.pk)


def forgot_password(request):
    request.title = _("Забыли пароль")
    form = ForgotPassword()
    if request.method == "POST":
        form = ForgotPassword(request.POST)
        if form.is_valid() and request.method == "POST":
            phone = form.cleaned_data["phone"]
            password = form.cleaned_data["new_password"]
            if User.objects.filter(phone=phone).exists():
                send_sms_code(request, phone)
                request.session["recovery"] = {
                    "phone": phone,
                    "new_password": password
                }
                get_code_form = GetCodeForm()
                return render(request, "main/get_code.html", {
                    "form": get_code_form,
                    "request.title": _("Отправить код")
                })
    return render(request, "main/forgot_password.html", {
        'form': form,
    })


@require_GET
def get_code(request):
    pass


@require_POST
def post_code(request):
    # request.title = "Отправить код"

    data = request.session.get("recovery")
    if request.method != "POST" or data["phone"] is None:
        return redirect('forgot_password')

    code = request.POST.get("code")

    if data["phone"] is None or not validate_sms_code(data["phone"], code):
        return False

    user = User.objects.get(phone=data["phone"])
    user.set_password(data["new_password"])
    user.save()

    return redirect("user:login")


