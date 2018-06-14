# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.conf.urls import include, url
from .views import *

app_name = 'projects'

urlpatterns = [
    url(r'(?P<slug>[\w-]+)/$', ProjectDetail.as_view(), name='project_detail'),
    url(r'category/(?P<slug>[\w-]+)/$', CategoryDetail.as_view(), name='category_detail'),
    url(r'', ProjectList.as_view(), name="project_list"),

]
