# -*- coding:utf-8 -*-
# author:h
# datetime:2019-07-26 21:45

from django import forms
from captcha.fields import CaptchaField
import redis

from imooc_oneline_imitate.settings import REDIS_HOST, REDIS_PORT
from apps.users.models import UserProfile


class RegisterGetForm(forms.Form):
    captcha = CaptchaField()


class RegisterPostForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)
    password = forms.CharField(required=True)

    def clean_mobile(self):
        mobile = self.data.get('mobile')
        # verify mobile number exiting or not
        users = UserProfile.objects.filter(mobile=mobile)
        if users:
            raise forms.ValidationError('This account already exist.')
        return mobile

    def clean_code(self):
        code = self.data.get('code')
        mobile = self.data.get('mobile')
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset='utf8', decode_responses=True)
        redis_code = r.get(str(mobile))

        if code != redis_code:
            raise forms.ValidationError('Verification is invalid.')

        return code


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)


class DynamicLoginForm(forms.Form):
    # myfield = AnyOtherField()
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    captcha = CaptchaField()


class DynamicLoginPostForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)

    def clean_code(self):
        mobile = self.data.get('mobile')
        code = self.data.get('code')

        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset='utf8', decode_responses=True)
        redis_code = r.get(str(mobile))

        if code != redis_code:
            raise forms.ValidationError('Verification is invalid.')

        return self.cleaned_data

    # def clean(self):
    #     mobile = self.cleaned_data['mobile']
    #     code = self.cleaned_data['code']
    #
    #     r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset='utf8', decode_responses=True)
    #     redis_code = r.get(str(mobile))
    #
    #     if code != redis_code:
    #         raise forms.ValidationError('Verification is invalid.')
    #
    #     return self.cleaned_data
