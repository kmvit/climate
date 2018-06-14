# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.conf.urls import include, url
from .views import *

app_name = 'project'

urlpatterns = [
    url(r'', ProjectList.as_view(), name="project_list"),
    url(r'projects/(?P<slug>[\w-]+)/$', ProjectDetail.as_view(), name='project_detail'),
]
