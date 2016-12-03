#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# Created by  on 2016/12/1

from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<pk>[0-9]+)/vote/$', views.vote, name='vote'),
]
