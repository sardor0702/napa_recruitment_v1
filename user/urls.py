from django.urls import path
# from .views import
from .views import UserRegistration, user_login, user_logout


app_name = "user"

urlpatterns = [
    path("registration/", UserRegistration.as_view(), name="registration"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout")
    # path('me/', Me.as_view()),
    # path("registration/", Registration.as_view())
]