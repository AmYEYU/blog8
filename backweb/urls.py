# encoding: utf-8
"""
@author: 叶玉
"""
from django.conf.urls import url

from backweb import views

urlpatterns = [
    # 注册
    url(r'^register/', views.register, name='register'),
    # 登录
    url(r'^login/', views.login, name='login'),
    # 退出
    url(r'^logout', views.logout, name='logout'),
    # 文章
    url(r'^article/', views.article, name='article'),
    # 添加文章
    url(r'^add_article/', views.add_article, name='add_article'),
    # 修改文章
    url(r'^update_article/(\d+)/', views.update_article, name='update_article'),
    # 删除文章
    url(r'^del_article/(\d+)/', views.del_article, name='del_article'),
    # 栏目
    url(r'^category/', views.category, name='category'),
    # 修改栏目
    url(r'^update_category/(\d+)/', views.update_category, name='update_category'),
    # 删除栏目
    url(r'^del_category/(\d+)/', views.del_category, name='del_category'),
    # 设置个人信息
    url(r'^user_modify_the/(\d+)/',views.user_modify_the, name='user_modify_the'),
]