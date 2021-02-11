from django.db import models
from user.models import User
# from student.models import Student


class Filter(models.Model):
    name = models.CharField(max_length=100)


class FilterValues(models.Model):
    filter_id = models.ForeignKey(Filter, on_delete=models.RESTRICT)
    value = models.TextField(max_length=2048)


class Query(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    student = models.ForeignKey('student.Student', on_delete=models.RESTRICT)
    added_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (('user', 'student'), )


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    student = models.ForeignKey('student.Student', on_delete=models.RESTRICT)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'student'), )
