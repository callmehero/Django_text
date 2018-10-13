# -*- coding:utf-8 -*-
# ！/usr/bin/env python
from django.core.mail import send_mail
from django_start.settings import EMAIL_FROM


def send_tip_mail(user_name, user_email, user_message):
    email_title = '来自用户"{}"的留言'.format(user_name)
    email_body = """
    他的联系邮箱是：{0}, 
    内容是：{1}
    """.format(user_email, user_message)
    # 管理员用户邮箱
    email = '506141737@qq.com'
    send_statue = send_mail(email_title, email_body, EMAIL_FROM, [email])  # 进源码以看就知道为什么要这样写
    try:
        if send_statue:
            return True
    except Exception as e:
        return None