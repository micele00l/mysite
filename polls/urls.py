#!/usr/bin/evn python
# -*- coding:utf-8 -*-
# Created by  on 2016/12/1

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
