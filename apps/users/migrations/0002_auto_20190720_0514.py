# Generated by Django 2.2 on 2019-07-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10, verbose_name='Gender'),
        ),
    ]
