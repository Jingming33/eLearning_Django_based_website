# Generated by Django 2.2 on 2019-07-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190720_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(max_length=15, verbose_name='mobile_number'),
        ),
    ]
