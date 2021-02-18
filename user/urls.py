from django.urls import path
from .views import UserRegistration, user_login, user_logout, login_checkin, user_info, user_info_post


app_name = "user"

urlpatterns = [
    path("registration/", UserRegistration.as_view(), name="registration"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("account/", login_checkin, name="personal_account"),
    path("info/<int:id>/", user_info, name="info"),
    path("info/save/", user_info_post, name="info_save"),
]
