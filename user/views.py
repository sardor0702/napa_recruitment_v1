from rest_framework.views import APIView
from .serializers import UserSerializer, RegistrationSerializer
# from napa_recruitment.responses import ResponseSuccess, ResponseFile
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegistrationForm, LoginForm
from .models import User
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
                return redirect('main:main_home')

            form.add_error('password', "Имя пользователя и пароль неверны !")
    return render(request, 'main/sign_in.html', {
        'form': form
    })


@login_required
def user_logout(request):
    logout(request)
    return redirect("main:sign_in")

# class UserRegistration(View):
#     def setup(self, request):
#
#     def get(self, request):
#
#         return render(request, 'main/sign_up.html')
#
# class Me(APIView):
#     def get(self, request):
#         return ResponseSuccess(UserSerializer(data=request.user).data)
#
#
# class Registration(APIView):
#     def post(self, request):
#         data = RegistrationSerializer(data=request.data)
#         if not data.is_valid():
#             return ResponseFile(data.data)
#
#         return ResponseSuccess("ok")
