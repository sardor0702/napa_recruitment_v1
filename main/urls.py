from django.urls import path, include

import main
from .views import Home, FavoritesView, Searching, student_card, save_fav, save_user,\
    favorite_delete, query_delete, filter_by_skills, handler404
from django.conf.urls import url, handler404


app_name = "main"

urlpatterns = [
    path('', Home.as_view(), name='main_home'),
    path("select2/", include("django_select2.urls")),  # django-select2
    path('favorites/', FavoritesView.as_view(), name="favorites"),
    path('favorite_delete/<int:id>/', favorite_delete, name='favorites_delete'),
    path('searching/', Searching.as_view(), name="searching"),
    path('student_card/<int:id>/', student_card, name="student_card"),
    path('save_fav/<int:id>/', save_fav, name='save_fav'),
    path('save_user/<int:id>/', save_user, name='save_user'),
    path('favorite_delete/<int:id>/', favorite_delete, name='favorites_delete'),
    path('query_delete/<int:id>/', query_delete, name='query_delete'),
    path('filter_by_skills/<str:slug>/', filter_by_skills, name='filter_by_skills'),
    url(r'^$', handler404, name='error')
]

handler404 = main.views.handler404
