from django.urls import path, include
from .views import Home, favorites, Searching, student_card

app_name = "main"

urlpatterns = [
    path('', Home.as_view(), name='main_home'),
    path('favorites/', favorites, name="favorites"),
    path('searching/', Searching.as_view(), name="searching"),
    path('student_card/<int:id>/', student_card, name="student_card"),

]
