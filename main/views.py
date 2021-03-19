from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, ListView
from student.models import Student, StudentProjects
from main.models import FilterValues, Filter, Favorite, Query
from .forms import SearchForm
from .seraializers import FavoriteSerializer
import json
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from rest_framework.response import Response
from django.db.models import Q


class Home(TemplateView):
    template_name = "main/home_page.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context


class Searching(ListView):
    template_name = "main/searching.html"
    paginate_by = 3
    model = Student

    def get_queryset(self):
        queryset = super().get_queryset()

        ids = list(map(int, self.request.GET.getlist('filter', [])))
        if len(ids) > 0:
            queryset = queryset.filter(filters__id__in=ids).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        k = str(self.request).split('?')[1].rstrip('\'>').split('&')
        t = ''
        for i in k:
            if not i.startswith('page'):
                t += '&' + i
        s = t.lstrip('&')
        context['k'] = s
        context['frontend'] = FilterValues.objects.filter(filter_id=2)
        context['backend'] = FilterValues.objects.filter(filter_id=1)
        context['title'] = _("Поиск")
        context['selected_filters'] = list(map(int, self.request.GET.getlist('filter')))

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
        context['title'] = _("Избранное")
        return context


def student_card(request, id):
    request.title = _("Студенческая страница")
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
    request.title = _("Сохранять")
    st = Student.objects.get(id=id)
    user = request.user
    if Favorite.objects.filter(student=st, user=user).exists():
        Favorite.objects.get(student=st, user=user).delete()
    else:
        Favorite.objects.create(student_id=st.id, user_id=user.id)

    return redirect("main:student_card", id=st.id)


def save_user(request, id):
    request.title = _("Сохранить пользователя")
    st = Student.objects.get(id=id)
    user = request.user
    if Query.objects.filter(student=st, user=user).exists():
        Query.objects.get(student=st, user=user).delete()
    else:
        Query.objects.create(student_id=st.id, user_id=user.id)

    return redirect("main:student_card", id=st.id)


def favorite_delete(request, id):
    current_favorite = Favorite.objects.get(id=id)
    current_favorite.delete()
    return redirect('main:favorites')


def get(request, id):
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
    get_obj = list(Student.objects.values().filter(Q(skills__contains=slug)))
    get_sp = list(StudentProjects.objects.values())
    return JsonResponse([get_obj, get_sp], safe=False)


def handler404(*args, **kwargs):
    text = render_to_string('main/404.html')
    return HttpResponseNotFound(text)

