from django.db import models
from main.models import FilterValues
from datetime import datetime
import os
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.conf import settings


def convert_fn(ins, file):
    ext = file.split('.')[-1]
    filename = '{:%Y-%m-%d-%H-%M-%S}.{}'.format(datetime.now(), ext)
    return os.path.join('student_pick', filename)


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

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @property
    def full_name(self):
        return "{} {}".format(self.last_name, self.first_name)

    def save(self, *args, **kwargs):
        if not self.student_image.closed:
            image = Image.open(self.student_image)
            image.thumbnail((1000, 1000), Image.ANTIALIAS)

            tmp = BytesIO()
            image.save(tmp, "PNG")

            self.student_image = File(tmp, 't.png')
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        if self.student_image:
            return os.path.join(settings.MEDIA_URL, str(self.student_image))

        return os.path.join(settings.STATIC_URL, "main/img/nophoto.png")


class StudentProjects(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.RESTRICT)
    project_link = models.CharField(max_length=255)
    created_at = models.DateField()
    project_pick = models.ImageField(upload_to=convert_fn, default=None)
