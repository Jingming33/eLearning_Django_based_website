# Generated by Django 2.2 on 2019-07-26 03:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Add Time'),
        ),
        migrations.AlterField(
            model_name='course',
            name='learn_time',
            field=models.IntegerField(default=0, verbose_name='total_learning_time (min)'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Add Time'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Add Time'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Add Time'),
        ),
    ]