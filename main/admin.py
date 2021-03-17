from django.contrib import admin
from .models import Query, Favorite, Filter, FilterValues, SmsCode

admin.site.site_header = "Admin for Napa Recruitment"

admin.site.register(Filter)
admin.site.register(FilterValues)


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'user_name', 'added_at']
    list_display_links = ['id', 'student_name', 'user_name', 'added_at']
    list_filter = ['added_at']
    search_fields = ['student_name', 'user_name']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'user_name', 'added_at']
    list_display_links = ['id', 'student_name', 'user_name', 'added_at']
    list_filter = ['added_at']



@admin.register(SmsCode)
class SmsCodeModelAdmin(admin.ModelAdmin):
    list_display = ['phone', 'code']
    search_fields = ('phone',)
