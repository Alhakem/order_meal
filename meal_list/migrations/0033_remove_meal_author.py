# Generated by Django 2.2 on 2019-05-22 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal_list', '0032_meal_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='author',
        ),
    ]
