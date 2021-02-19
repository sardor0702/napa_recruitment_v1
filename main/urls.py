from django.urls import path, include
from .views import Home

app_name = "main"

urlpatterns = [
    path('', Home.as_view(), name='main_home'),
]