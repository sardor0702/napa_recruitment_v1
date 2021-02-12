from django.urls import path
from .views import Me, Registration

urlpatterns = [
    path('me/', Me.as_view()),
    path("registration/", Registration.as_view())
]