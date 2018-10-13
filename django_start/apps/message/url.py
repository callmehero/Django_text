# -*- coding:utf-8 -*-
# ！/usr/bin/env python
from django.conf.urls import url, include
from .views import MessageView

urlpatterns = [
    url(r'^message/$', MessageView.as_view(), name='user_message'),
]
