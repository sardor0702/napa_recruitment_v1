from django import template

register = template.Library()

@register.filter
def limit(query, limit):
    return query[:limit]
