from django.db import models
from user.models import User


# from student.models import Student


# class Category(models.Model):
#     name = models.CharField(max_length=256)


class Filter(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FilterValues(models.Model):
    filter_id = models.ForeignKey(Filter, on_delete=models.RESTRICT)
    value = models.TextField(max_length=2048)

    def __str__(self):
        return self.value


class Query(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    student = models.ForeignKey('student.Student', on_delete=models.RESTRICT)
    added_at = models.DateTimeField(auto_now_add=True)

    def student_name(self):
        return self.student.full_name

    def user_name(self):
        return self.user.username

    class Meta:
        unique_together = (('user', 'student'),)

    def __str__(self):
        return str(self.user_id) + " | " + self.student.full_name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50, blank=True, null=True)
    student = models.ForeignKey('student.Student', on_delete=models.RESTRICT)
    added_at = models.DateTimeField(auto_now_add=True)

    def student_name(self):
        return self.student.full_name

    def user_name(self):
        return self.user.username

    def __str__(self):
        return str(self.user.id) + " | " + self.student.full_name + " | " + str(self.added_at)

    class Meta:
        unique_together = (('user', 'student'),)


class SmsCode(models.Model):
    phone = models.CharField(max_length=16, db_index=True)
    ip = models.GenericIPAddressField(db_index=True)
    code = models.CharField(max_length=10)
    expire_at = models.DateTimeField(db_index=True)

    class Meta:
        index_together = []


class SmsAttempt(models.Model):
    phone = models.CharField(max_length=16, db_index=True)
    counter = models.IntegerField(default=0)
    last_attempt_at = models.DateTimeField(db_index=True)
