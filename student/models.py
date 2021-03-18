import base64

import qrcode
from django.db import models
from main.models import FilterValues
from datetime import datetime
import os
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.conf import settings
from django.urls import reverse
from django.utils.safestring import mark_safe

from napa_recruitment.settings import SITE_DOMAIN


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

    def admin_image(self):
        return mark_safe('<img src="{}" width="60" />'.format(self.student_image.url))

    def qr(self):
        url = f'{SITE_DOMAIN}/student_card/{self.pk}/'
        print(url)
        qr = qrcode.make(url)
        buffered = BytesIO()
        qr.save(buffered, format='PNG')
        img_str = base64.b64encode(buffered.getvalue())
        img_str = img_str.decode("utf-8")

        return mark_safe(f'<img width="100px" src="data:image/png;base64, {img_str}"/>')

    admin_image.short_description = "Student image"
    admin_image.allow_tags = True

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('main:student_card', kwargs={'id': self.id})

    @property
    def full_name(self):
        return "{} {}".format(self.last_name, self.first_name)

    @property
    def projects_top3(self):
        return self.projects.all()[:3]

    @property
    def projects_top4(self):
        return self.projects.all()[:4]

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
    student_id = models.ForeignKey(Student, on_delete=models.RESTRICT, related_name='projects')
    project_name = models.CharField(max_length=255, default=None, blank=True)
    project_link = models.CharField(max_length=255)
    created_at = models.DateField()
    project_pick = models.ImageField(upload_to=convert_fn, default=None)

    # def admin_pro_pick(self):
    #     return mark_safe('<img src="{}" width="120" />'.format(self.project_pick.url))
    # admin_pro_pick.short_description = "Project pick"
    # admin_pro_pick.allow_tags = True

    def __str__(self):
        return str(self.student_id) + ' | ' + self.project_name + ' | ' + self.project_link

    @property
    def image_url(self):
        if self.project_pick:
            return os.path.join(settings.MEDIA_URL, str(self.project_pick))

        return os.path.join(settings.STATIC_URL, "main/img/nophoto.png")

    class Meta:
        verbose_name = 'student project'
        verbose_name_plural = 'student projects'
