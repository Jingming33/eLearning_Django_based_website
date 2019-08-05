from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENDER_CHOICE = (
    ('male', 'male'),
    ('female', 'female')
)


class BaseModel(models.Model):
    add_time = models.DateField(verbose_name='Add Time', default=datetime.now)

    class Meta:
        abstract = True


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='Nick Name', default='')
    day_birth = models.DateField(verbose_name='Birthday', null=True, blank=True)
    gender = models.CharField(max_length=10, verbose_name='Gender', choices=GENDER_CHOICE)
    address = models.CharField(max_length=100, verbose_name='Address', default='')
    mobile = models.CharField(max_length=15, verbose_name='mobile_number')
    image = models.ImageField(upload_to='head_image/%Y%m', verbose_name='profile_image', default='default.jpg')

    class Meta:
        verbose_name = 'User Information'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username



