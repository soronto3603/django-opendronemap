# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import list,start_recon

urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^start/$',start_recon,name='start_recon'),
]
