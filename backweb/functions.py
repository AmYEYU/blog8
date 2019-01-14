# encoding: utf-8
"""
@author: 叶玉
"""

# 装饰器，闭包

# 1. 外层函数内嵌内层函数
# 2. 外层函数返回内层函数
# 3. 内层函数调用外层函数的参数
from django.http import HttpResponseRedirect
from django.urls import reverse


def is_login(func):
    def check_stats(request):
        if request.session.get('user_id'):
            return func(request) #index()
        else:
            return HttpResponseRedirect(reverse('user:my_login'))
    return check_stats