from django.db import models

from apps.users.models import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=20, verbose_name='City Name')
    desc = models.CharField(max_length=200, verbose_name='Description')

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            raise ValueError('Name is None here')


class CourseOrg(BaseModel):
    name = models.CharField(max_length=50, verbose_name='name_of_organization')
    desc = models.TextField(verbose_name='description')
    tag = models.CharField(default='national_popular', max_length=20, verbose_name='tag_organization')
    category = models.CharField(default='training_camp', verbose_name='organization_type', max_length=10,
                                choices=(('tc', 'training_camp'), ('pe', 'personal'), ('hr', 'high_rank_school')))
    click_nums = models.IntegerField(default=0, verbose_name='clicked_times')
    fav_nums = models.IntegerField(default=0, verbose_name='subscribe_number')
    image = models.ImageField(upload_to='org/%Y%m', verbose_name=u'logo', max_length=100)
    address = models.CharField(max_length=150, verbose_name='address_organization')
    students = models.IntegerField(default=0, verbose_name='learning_students_count')
    course_nums = models.IntegerField(default=0, verbose_name='nums_of_chapters')

    # CourseOrg have directly relate with city, which define city as a foreignkey
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=u'location_of_city')

    class Meta:
        verbose_name = 'course_organization'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            raise ValueError('Name is None here')


class Teacher(BaseModel):
    # Teacher have directly relate with CourseOrg, which define CourseOrg as a foreignkey
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name='belong_to_organization')
    name = models.CharField(max_length=50, verbose_name=u'teacher_name')
    work_year = models.IntegerField(default=0, verbose_name='years_of_work')
    word_company = models.CharField(max_length=50, verbose_name='work_company')
    work_position = models.CharField(max_length=50, verbose_name='position_work')
    points = models.CharField(max_length=50, verbose_name='teaching_character')
    click_nums = models.IntegerField(default=0, verbose_name='clicked_time')
    fav_nums = models.IntegerField(default=0, verbose_name='subscribe_number')
    age = models.IntegerField(default=18, verbose_name='age')
    image = models.ImageField(upload_to='teacher/%Y%m', verbose_name='teacher_img', max_length=100)

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            raise ValueError('Name is None here')
