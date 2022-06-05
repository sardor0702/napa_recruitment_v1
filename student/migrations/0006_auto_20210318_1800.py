# Generated by Django 3.1.6 on 2021-03-18 18:00

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20210318_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='skills',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_about',
            field=models.TextField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_image',
            field=models.ImageField(blank=True, null=True, upload_to=student.models.convert_fn),
        ),
    ]
