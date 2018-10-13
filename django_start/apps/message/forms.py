# -*- coding:utf-8 -*-
# ！/usr/bin/env python
from django.forms import ModelForm
from .models import Message


class UserMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'address', 'comment']
