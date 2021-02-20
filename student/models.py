from django.db import models
from main.models import FilterValues
from datetime import datetime
import os

def convert_fn(ins, file):
    ext = file.split('.')[-1]
    filename = '{:%Y-%m-%d-%H-%M-%S}.{}'.format(datetime.now(), ext)
    return os.path.join('student_pick',filename)

class Student(models.Model):
    filters = models.ManyToManyField(FilterValues)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    direction = models.CharField(max_length=100)
    skills = models.CharField(max_length=255)
    age = models.IntegerField()
    student_about = models.TextField(max_length=2048, blank=True)
    student_image = models.ImageField(upload_to=convert_fn)
    status = models.IntegerField(default=0)


class StudentProjects(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.RESTRICT)
    project_link = models.CharField(max_length=255)
    created_at = models.DateField()
    project_pick = models.ImageField(upload_to=convert_fn)