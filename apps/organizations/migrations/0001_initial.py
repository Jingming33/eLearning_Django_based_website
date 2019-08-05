# Generated by Django 2.2 on 2019-07-20 03:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='add_current_time')),
                ('name', models.CharField(max_length=20, verbose_name='city')),
                ('desc', models.CharField(max_length=200, verbose_name='description')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'city',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='add_current_time')),
                ('name', models.CharField(max_length=50, verbose_name='name_of_organization')),
                ('desc', models.TextField(verbose_name='description')),
                ('tag', models.CharField(default='National_popular', max_length=20, verbose_name='tag_organization')),
                ('category', models.CharField(choices=[('tc', 'traning_camp'), ('pe', 'personal'), ('hr', 'high_rank_school')], default='training_camp', max_length=10, verbose_name='organization_type')),
                ('click_nums', models.IntegerField(default=0, verbose_name='clicked_times')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='subscribe_number')),
                ('image', models.ImageField(upload_to='org/%Y%m', verbose_name='logo')),
                ('address', models.CharField(max_length=150, verbose_name='address_organization')),
                ('students', models.IntegerField(default=0, verbose_name='learning_students_count')),
                ('course_nums', models.IntegerField(default=0, verbose_name='nums_of_chapters')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.City', verbose_name='location_of_city')),
            ],
            options={
                'verbose_name': 'course_organization',
                'verbose_name_plural': 'course_organization',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='add_current_time')),
                ('name', models.CharField(max_length=50, verbose_name='teacher_name')),
                ('work_year', models.IntegerField(default=0, verbose_name='years_of_work')),
                ('word_company', models.CharField(max_length=50, verbose_name='work_company')),
                ('work_position', models.CharField(max_length=50, verbose_name='position_work')),
                ('points', models.CharField(max_length=50, verbose_name='teaching_character')),
                ('click_nums', models.IntegerField(default=0, verbose_name='clicked_time')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='subscribe_number')),
                ('age', models.IntegerField(default=18, verbose_name='age')),
                ('image', models.ImageField(upload_to='teacher/%Y%m', verbose_name='teacher_img')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.CourseOrg', verbose_name='belong_to_organization')),
            ],
            options={
                'verbose_name': 'teacher',
                'verbose_name_plural': 'teacher',
            },
        ),
    ]
