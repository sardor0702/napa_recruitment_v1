from django.urls import path, include
from .views import Home, FavoritesView, Searching, student_card, save_fav, save_user, favorite_delete

app_name = "main"

urlpatterns = [
    path('', Home.as_view(), name='main_home'),
    path("select2/", include("django_select2.urls")),  # django-select2
    path('favorites/', FavoritesView.as_view(), name="favorites"),
    path('favorite_delete/<int:id>/', favorite_delete, name='favorites_delete'),
    path('searching/', Searching.as_view(), name="searching"),
    path('student_card/<int:id>/', student_card, name="student_card"),
    path('save_fav/<int:id>/', save_fav, name='save_fav'),
    path('save_user/<int:id>/', save_user, name='save_user')
]
