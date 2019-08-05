from django.db import models

from apps.users.models import BaseModel
from apps.organizations.models import Teacher


# Create your models here.

class Course(BaseModel):
    # course have directly relate with teacher, which define teacher as a foreignkey
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Teacher')

    name = models.CharField(verbose_name='course_name', max_length=50)
    desc = models.CharField(verbose_name='course_description', max_length=300)
    learn_time = models.IntegerField(default=0, verbose_name='total_learning_time (min)')
    degree = models.CharField(verbose_name='difficult',
                              choices=(('bg', 'beginner'), ('im', 'intermediate'), ('ep', 'expert')), max_length=2)
    student = models.IntegerField(default=0, verbose_name='learning_student_current')
    fav_number = models.IntegerField(default=0, verbose_name='subscribe_number')
    click_number = models.IntegerField(default=0, verbose_name='clicked_number')
    category = models.CharField(default='backend_develop', max_length=20, verbose_name='class_type')
    tag = models.CharField(default='', max_length=10, verbose_name='class_tag')
    class_info = models.CharField(default='', max_length=300, verbose_name='class_general_intro')
    teacher_reg = models.CharField(default='', max_length=300, verbose_name='recommendation')

    detail = models.TextField(verbose_name='class_detail')
    image = models.ImageField(upload_to='course/%Y%m', verbose_name='cover_image', max_length=100)

    class Meta:
        verbose_name = 'Course_Info'
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     if self.name:
    #         return self.name
    #     else:
    #         raise ValueError('Name is None here')


class Lesson(BaseModel):
    # Lesson have directly relate with Course, which define course as a foreignkey
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, verbose_name='chapter_name')
    learn_time = models.IntegerField(default=0, verbose_name='total_learning_time(mins)')

    class Meta:
        verbose_name = 'Lesson_Chapter'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            raise ValueError('Name is None here')


class Video(BaseModel):
    # video have directly relate with Lesson, which define lesson as a foreignkey
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='chapter')

    name = models.CharField(max_length=100, verbose_name='video_name')
    learn_time = models.IntegerField(default=0, verbose_name='total_learning_time(mins)')
    url = models.URLField(max_length=200, verbose_name='video_url_address')  # cannot be none

    class Meta:
        verbose_name = 'uploaded_video'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            raise ValueError('Name is None here')


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='course_resource')
    name = models.CharField(max_length=100, verbose_name='resource_download')
    file = models.FileField(upload_to='course/resource/%Y%m', verbose_name='download_address', max_length=200)

    class Meta:
        verbose_name = 'Course_Resource'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            raise ValueError('Name is None here')
