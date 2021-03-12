from django.contrib import admin
from .models import Query, Favorite, Filter, FilterValues, SmsCode

admin.site.register(Filter)
admin.site.register(FilterValues)
admin.site.register(Query)
admin.site.register(Favorite)


@admin.register(SmsCode)
class SmsCodeModelAdmin(admin.ModelAdmin):
    list_display = ['phone', 'code']
