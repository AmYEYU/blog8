# encoding: utf-8
"""
@author: 叶玉
"""
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from backweb.models import User


class TestMiddlware1(MiddlewareMixin):
    # 中间键
    def process_request(self, request):
        # 对所有请求进行登录状态的校验
        url = request.path
        if url in ['/backweb/register/','/backweb/login/']:
            # 跳过列表中的代码，直接访问路由对应的视图函数
            return None
        try:
            user_id = request.session['user_id']
            user = User.objects.get(pk=user_id)
            request.user = user
            return None
        except Exception as e:
            return HttpResponseRedirect(reverse('backweb:login'))

