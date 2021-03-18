from django.contrib import admin
from .models import Student, StudentProjects


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "admin_image", "qr", "first_name", "last_name", "age", "skills", "status")
    list_display_links = ('id', "admin_image", 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'skills', 'age')


@admin.register(StudentProjects)
class StudentProjectsAdmin(admin.ModelAdmin):
    list_display = ("id", "project_name", "project_pick", "project_link", "student_id_id", "created_at")
    list_display_links = ("id", "project_name", "project_link", "student_id_id")
    list_filter = ("created_at",)
    search_fields = ("project_name",)

