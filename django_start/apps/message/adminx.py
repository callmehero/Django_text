# -*- coding:utf-8 -*-
# ！/usr/bin/env python
import xadmin
from message.models import Message
from xadmin.views import BaseAdminView, CommAdminView

class GlobalSetting(object):
    site_title = '用户留言信息管理系统'
    site_footer = 'power@by:Zisc'
    menu_style = 'accordion'

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class MessageAdmin(object):
    list_display = ['name', 'email', 'address', 'comment', 'add_time']
    search_fields = ['name', 'email', 'address', 'comment']
    list_filter = ['name', 'email', 'address', 'comment', 'add_time']


xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(BaseAdminView, BaseSetting)
xadmin.site.register(CommAdminView, GlobalSetting)