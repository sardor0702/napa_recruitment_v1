from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name", "phone", "mobil_phone", "email", "company_name", "activity_company")
    list_display_links = ('id', 'username', 'first_name', 'last_name')
    list_filter = ("date_joined",)
    search_fields = ("username", "phone")
