from django.shortcuts import render
from django.views.generic import View
from .forms import UserMessageForm
from django.http import HttpResponse
from utils.email_send import send_tip_mail

# Create your views here.

class MessageView(View):
    def get(self, request):
        return render(request, '留言板.html')

    def post(self, request):
        user_post_form = UserMessageForm(request.POST)
        if user_post_form.is_valid():
            user_name = request.POST.get('name', '')
            user_message = request.POST.get('comment', '')
            user_email = request.POST.get('email', '')
            user_post_form.save(commit=True)
            # 如果有用户提交会给管理员发个邮箱提醒
            send_status_code = send_tip_mail(user_name, user_email, user_message)
            if send_status_code:
                return HttpResponse('{"status": "success", "msg": "提交成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "提交出错，请提交符合规范的内容"}', content_type='application/json')