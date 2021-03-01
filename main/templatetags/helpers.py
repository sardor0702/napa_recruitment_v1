from django import template
from main.models import Favorite
from student.models import Student

register = template.Library()

@register.filter
def limit(query, limit):
    return query[:limit]

