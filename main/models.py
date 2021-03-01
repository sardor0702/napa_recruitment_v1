from django.db import models
from user.models import User
# from student.models import Student


class Filter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FilterValues(models.Model):
    filter_id = models.ForeignKey(Filter, on_delete=models.RESTRICT)
    value = models.TextField(max_length=2048)

    def __str__(self):
        return self.value+' '+str(self.filter_id)


class Query(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    student = models.ForeignKey('student.Student', on_delete=models.RESTRICT)
    added_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (('user', 'student'), )


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50, blank=True, null=True)
    student = models.ForeignKey('student.Student', on_delete=models.RESTRICT)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        unique_together = (('user', 'student'), )
