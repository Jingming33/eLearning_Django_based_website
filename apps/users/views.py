from django.shortcuts import render
from django.views.generic.base import View  # get and post
from django.contrib.auth import authenticate, login, logout  # verify the password and username
from django.http import HttpResponseRedirect, JsonResponse  # redirect the login page to index
from django.urls import reverse  # redirect the login page to index (better one)

import redis

from apps.users.forms import LoginForm, DynamicLoginForm, DynamicLoginPostForm
from apps.users.forms import RegisterGetForm, RegisterPostForm
# from apps.utils.Text_Verify import send_single_sms
from apps.utils.fake_text_verify import send_single_sms
from apps.utils.random_str import generate_random
from imooc_oneline_imitate.settings import client, REDIS_HOST, REDIS_PORT
from apps.users.models import UserProfile


class LoginView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))

        login_form = DynamicLoginForm()

        return render(request, 'login.html', {
            'login_form': login_form
        })

    def post(self, request, *args, **kwargs):
        # user_name = request.POST.get('username', '')
        # password = request.POST.get('password', '')

        # if not user_name:
        #     return render(request, 'login.html', {'msg': 'Please fill in user name'})
        # if not password:
        #     return render(request, 'login.html', {'msg': 'Please fill in password'})

        '''form checking'''

        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=user_name, password=password)

            #  check the user and password is exist or not
            if user is not None:
                # get the user
                login(request, user)

                # if success, return to index.html
                # return render(request, 'index.html')

                return HttpResponseRedirect(reverse('index'))

            else:
                # if not find user
                return render(request, 'login.html',
                              {'msg': 'User name or password is not valid', 'login_form': login_form})


        else:
            return render(request, 'login.html', {'login_form': login_form})


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class SendSmsView(View):
    def post(self, request, *args, **kwargs):
        send_sms_form = DynamicLoginForm(request.POST)
        re_dict = {}

        if send_sms_form.is_valid():
            mobile = send_sms_form.cleaned_data['mobile']
            code = generate_random(4, 0)
            re_json = send_single_sms(client, code, mobile=mobile)
            if re_json['code'] == 0:
                re_dict['status'] = 'success'
                r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset='utf8', decode_responses=True)
                r.set(mobile, code)
                r.expire(str(mobile), 60 * 5)  # 5 mins expire

            else:
                re_dict['msg'] = re_json['msg']

        else:
            for key, value in send_sms_form.errors.items():
                re_dict[key] = value[0]

        return JsonResponse(re_dict)


class DynamicLoginView(View):
    def post(self, request, *args, **kwargs):
        login_form = DynamicLoginPostForm(request.POST)
        dynamic_login = True

        if login_form.is_valid():
            # without register account, still can login
            mobile = login_form.cleaned_data['mobile']
            existed_users = UserProfile.objects.filter(mobile=mobile)

            if existed_users:
                user = existed_users[0]
            else:
                # create new user
                user = UserProfile(username=mobile)
                password = generate_random(10, 2)
                user.set_password(password)
                user.mobile = mobile
                user.save()

            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            d_form = DynamicLoginForm()
            return render(request, 'login.html', {'login_form': login_form,
                                                  'd_form': d_form,
                                                  'dynamic_login': dynamic_login})


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        register_get_form = RegisterGetForm()
        return render(request, 'register.html', {
            'register_get_form': register_get_form,
        })

    def post(self, request, *args, **kwargs):
        register_post_form = RegisterPostForm(request.POST)
        # dynamic_login = True

        if register_post_form.is_valid():
            mobile = register_post_form.cleaned_data['mobile']
            password = register_post_form.cleaned_data['password']

            # create new user
            user = UserProfile(username=mobile)
            user.set_password(password)
            user.mobile = mobile
            user.save()

            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            register_get_form = RegisterGetForm()
            return render(request, 'register.html', {'register_get_form': register_get_form,
                                                     'register_post_form': register_post_form})
