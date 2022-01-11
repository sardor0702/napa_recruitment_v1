# Generated by Django 3.1.6 on 2021-02-22 12:02

from django.db import migrations, models
import napa_recruitment.validators
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210212_1401'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=user.models.convert_fn),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(help_text='Пожалуйста, предоставьте свой телефон', max_length=15, unique=True, validators=[napa_recruitment.validators.PhoneValidator]),
        ),
    ]
