# -*- coding:utf-8 -*-
# author:h
# datetime:2019-07-21 15:01

import xadmin

from apps.organizations.models import City, CourseOrg, Teacher


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_year', 'word_company']
    search_fields = ['org', 'name', 'work_year', 'word_company']
    list_filter = ['org', 'name', 'work_year', 'word_company']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums']


class CityAdmin(object):
    list_display = ['id', 'name', 'desc']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    list_editable = ['name', 'desc']


xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(City, CityAdmin)
