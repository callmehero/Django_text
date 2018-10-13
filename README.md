# django-1.11 案例
> 闲来无事用django1.11写了一个练手的小玩具 

## 功能如下：
- 定义了一个用户留言板的功能
- 在用户留言后后台会自动给管理者发送邮件提醒
- 搭建了xadmin的后台管理系统  
  
## 演示：
根据我url的配置，需要访问http://127.0.0.1:8000/add/message/  
![image](https://github.com/callmehero/Django_text/blob/master/readme_material/view.png)  
- **错误提交**  
当进行错误提交时，比如什么都不填，直接提交这会有错误弹窗提示，如下：  
![image](https://github.com/callmehero/Django_text/blob/master/readme_material/error_tip.png)  
- **正确演示**  
当你填写了正确的数据时，提交后会有正确的提示，显示提交成功，如下，并且你会在你所设置的管理员邮箱中接收到该留言信息，如下：  
![image](https://github.com/callmehero/Django_text/blob/master/readme_material/success_tip.png)
![image](https://github.com/callmehero/Django_text/blob/master/readme_material/receive_message.png)

我们还可以从后台管理系统中查看到该记录的信息，访问http://127.0.0.1:8000/xadmin/ (在此之前要先注册好超级管理员用户，用于登录)  
![image](https://github.com/callmehero/Django_text/blob/master/readme_material/message_info.png)

## **使用提示**  
> 启动之前：  
1-调用makemigrations生成表   
2-调用migrate合成表  
3-在启动xadmin时需要安装好各种依赖  
可能需要安装的依赖：

模块 | 命令
---|---
future | pip install future
crispy-forms | pip install django-crispy-forms
formtools | pip install django-formtools  
six | pip install six
httplib2 | pip install httplib2  
可能不齐全，如果报错需要根据具体报错信息来进行调整
  
---  
> 关于邮箱的一些配置  
在setting.py中定义了利用django发送EMAIL所需的属性，如下：  
![image](https://github.com/callmehero/Django_text/blob/master/readme_material/setting_email.png)  
在 **django/extra_apps/utils/email_send.py**。中定义了我们的发送邮件函数。下面做一个简单的说明：  
![image](https://github.com/callmehero/Django_text/blob/master/readme_material/email_send.png)
