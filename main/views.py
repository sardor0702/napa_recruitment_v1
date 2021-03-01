from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, ListView
from student.models import Student, StudentProjects
from main.models import FilterValues, Filter, Favorite, Query
from .forms import SearchForm


class Home(TemplateView):
    template_name = "main/home_page.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context


def favorites(request):
    request.title = _("Избранное")
    return render(request, 'main/favorites.html')


class Searching(ListView):
    template_name = "main/searching.html"
    paginate_by = 3

    def get_queryset(self):
        return Student.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fontend'] = FilterValues.objects.filter(filter_id_id=4)
        context['backend'] = FilterValues.objects.filter(filter_id_id=3)

        return context


def student_card(request, id):
    request.title = _("")
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return redirect('searching')
    k = Favorite.objects.filter(student_id=student.id)
    query = Query.objects.filter(student_id=student.id)
    test_q = ''
    t = ''
    for i in k:
        t = i
    for i in query:
        test_q = i

    return render(request, "main/student_card.html", {
        'student': student,
        'fav': t,
        'test_query': test_q
    })


def save_fav(request, id):
    request.title = _("save")
    print(request.user)
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
    if not Query.objects.filter(student_id=st, user=user).exists():
        Query.objects.create(student_id=st.id, user_id=user.id)

    return redirect("main:student_card", id=st.id)
