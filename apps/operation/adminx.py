# -*- coding:utf-8 -*-
# author:h
# datetime:2019-07-21 17:09

import xadmin

from apps.operation.models import UserAsk, UserCourse, UserMessage, CourseComments, UserFavorite


# redesign font and footer
class GlobalSetting(object):
    site_title = 'imooc_online_system'
    site_footer = 'imooc_online_education'
    # menu_style = 'accordion'


# enable different xadmin theme
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'add_time']
    list_filter = ['user', 'course', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'add_time']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'add_time']
    list_filter = ['user', 'course', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'add_time']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)

# redesign the font and footer
xadmin.site.register(xadmin.views.CommAdminView, GlobalSetting)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)
