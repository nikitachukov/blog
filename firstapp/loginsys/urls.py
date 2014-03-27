#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nikitos'


from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login/', 'loginsys.views.login'),
    url(r'^logout/', 'loginsys.views.logout'),
)
