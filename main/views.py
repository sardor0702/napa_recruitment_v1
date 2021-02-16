from django.shortcuts import render, redirect
from . import views
from .forms import RegisterForm, LoginForms
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.decorators import login_required
from user.models import User


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


def logout_check(request):
    logout(request)
    return redirect("main_login")


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


def update(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return redirect('main_checkin')

    if request.method == 'POST':
        user.company_name = request.POST.get('company_name')
        name = request.POST.get('full_name').strip()
        user.first_name, user.last_name = name.split()
        user.activity_company = request.POST.get('activity_company')
        user.phone = request.POST.get('phone')
        user.mobil_phone = request.POST.get('mobil_phone')
        user.email = request.POST.get('email')
        user.save()
        return redirect('main_checkin')
    return render(request, 'main/personal_account_changing_info.html', {
        'user': user
    })

# def user_info_update(request):
#     form = UserForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = UserForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, "main/personal_account.html", context=context)



