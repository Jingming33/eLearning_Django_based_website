from django.db import models

from django.contrib.auth import get_user_model

from apps.users.models import BaseModel
from apps.courses.models import Course

UserProfile = get_user_model()


class UserAsk(BaseModel):
    name = models.CharField(max_length=20, verbose_name='name')
    mobile = models.CharField(max_length=15, verbose_name='phone_number')
    course_name = models.CharField(max_length=50, verbose_name=u'course_name')

    class Meta:
        verbose_name = 'User_inquire'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{name}_{course}({mobile})'.format(name=self.name, course=self.course_name, mobile=self.mobile)


class CourseComments(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='users')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='course')
    comments = models.CharField(max_length=200, verbose_name='comments')

    class Meta:
        verbose_name = 'course_comments'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.comments:
            return self.comments
        else:
            raise ValueError('No comments')


class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='users')
    fav_id = models.IntegerField(verbose_name='digital_id')
    fav_type = models.IntegerField(choices=((1, 'course'), (2, 'course_oganization'), (3, 'teacher')), default=1,
                                   verbose_name=u'subscribe_type')

    class Meta:
        verbose_name = 'user_subscribe'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{user}_{id}'.format(user=self.user.username, id=self.fav_id)


class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='users')
    message = models.CharField(max_length=200, verbose_name='user_message')
    has_read = models.BooleanField(default=False, verbose_name='read_or_unread')

    class Meta:
        verbose_name = 'user_msg'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.message:
            return self.message
        else:
            raise ValueError('No Messages')


class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='users')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='course')

    class Meta:
        verbose_name = 'user_course'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.course.name:
            return self.course.name
        else:
            raise ValueError('No course name')
