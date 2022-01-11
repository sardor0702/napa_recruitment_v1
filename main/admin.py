from django.contrib import admin
from .models import Query,Favorite,Filter,FilterValues

admin.site.register(Filter)
admin.site.register(FilterValues)
admin.site.register(Query)
admin.site.register(Favorite)
# Register your models here.
