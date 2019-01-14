# encoding: utf-8
"""
@author: 叶玉
"""
from django.conf.urls import url

from web import views

urlpatterns = [
    # 首页
    url(r'index/', views.index, name='index'),
    # 关于我
    url(r'^about/', views.about, name='about'),
    # 博客文章
    url(r'^list/', views.list, name='list'),
    # 文章详情
    url(r'^info/(\d+)/', views.info, name='info'),

]