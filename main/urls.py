from django.urls import path, include
from .views import Home, favorites, searching

app_name = "main"

urlpatterns = [
    path('', Home.as_view(), name='main_home'),
    path('favorites/', favorites, name="favorites"),
    path('searching/', searching, name="searching"),
]
