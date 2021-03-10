from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, ListView
from student.models import Student, StudentProjects
from main.models import FilterValues, Filter, Favorite, Query
from .forms import SearchForm
from .seraializers import FavoriteSerializer
import json
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q


class Home(TemplateView):
    template_name = "main/home_page.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context


# def favorites(request):
#     request.title = _("Избранное")
#     user = request.user
#
#     return render(request, 'main/favorites.html')


class Searching(FilterValues, ListView):
    template_name = "main/searching.html"
    paginate_by = 3

    def get_queryset(self):
        return Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fontend'] = FilterValues.objects.filter(filter_id=6)
        context['backend'] = FilterValues.objects.filter(filter_id=7)

        return context


class FavoritesView(ListView):
    template_name = "main/favorites.html"
    paginate_by = 3

    def get_queryset(self):
        return Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favorites'] = Favorite.objects.filter()
        context['querys'] = Query.objects.all()
        return context


def student_card(request, id):
    request.title = _("")
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return redirect('searching')

    t = 0
    k = Favorite.objects.filter(user_id=request.user.id, student_id=student.id).last()
    if k:
        t = k.id

    sent_query = Query.objects.filter(user_id=request.user.id, student_id=student.id).exists()

    return render(request, "main/student_card.html", {
        'student': student,
        'fav': t,
        'sent_query': sent_query
    })


def save_fav(request, id):
    request.title = _("save")
    st = Student.objects.get(id=id)
    user = request.user
    if Favorite.objects.filter(student=st, user=user).exists():
        Favorite.objects.get(student=st, user=user).delete()
    else:
        Favorite.objects.create(student_id=st.id, user_id=user.id)

    return redirect("main:student_card", id=st.id)


def save_user(request, id):
    request.title = _("")
    st = Student.objects.get(id=id)
    user = request.user
    # if not Query.objects.filter(student_id=st, user=user).exists():
    #     Query.objects.create(student_id=st.id, user_id=user.id)
    if Query.objects.filter(student=st, user=user).exists():
        Query.objects.get(student=st, user=user).delete()
    else:
        Query.objects.create(student_id=st.id, user_id=user.id)

    return redirect("main:student_card", id=st.id)


def favorite_delete(request, id):
    current_favorite = Favorite.objects.get(id=id)
    current_favorite.delete()
    return redirect('main:favorites')


# def get_all_favorites(request, id):
#     fav = Favorite.objects.filter(user_id=id)
#     serializer = FavoriteSerializer(fav, many=True)
#     print(serializer.data)
#     return JsonResponse(serializer.data)

def get(request, id):
    print(id)
    fav = Favorite.objects.filter(user_id=id)
    serializer = FavoriteSerializer(fav, many=True)
    return Response(serializer.data)


def favorite_delete(request, id):
    '''
        Removes student info from users favorite list
    '''
    current_favorite = Favorite.objects.get(id=id)
    data = list(Favorite.objects.values().filter(user_id=request.user, id=id))
    current_favorite.delete()
    return JsonResponse(data, safe=False)

def query_delete(request, id):
    '''
        Removes student info from users order list
    '''
    current_query = Query.objects.get(id=id)
    data = list(Query.objects.values().filter(user_id=request.user, id=id))
    current_query.delete()
    return JsonResponse(data, safe=False)


def filter_by_skills(request, slug):
    # print(slug)
    get_obj = list(Student.objects.values().filter(Q(skills__contains=slug)))
    get_sp = list(StudentProjects.objects.values())
    # print(Student.objects.values())
    return JsonResponse([get_obj, get_sp], safe=False)



#
# class FilterView(ListView):
#     def get_queryset(self):
#         queryset = FilterValues.objects.filter(value__in=self.request.GET.getlist("value"))
#         return queryset