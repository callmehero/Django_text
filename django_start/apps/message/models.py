from django.db import models
from datetime import datetime

# Create your models here.

class Message(models.Model):
    # model的字段中CharField字段，必须设定max_length最大长度这个参数
    name = models.CharField(max_length=20, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=30, verbose_name='住址')
    comment = models.TextField(max_length=200, verbose_name='留言')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '留言信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name