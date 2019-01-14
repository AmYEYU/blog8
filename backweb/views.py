import random

from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from backweb.models import User, UserToken, Article, Column
from django.urls import reverse


def register(request):
    # 注册
    if request.method == 'GET':
        return render(request, 'backweb/register.html')
    if request.method == 'POST':
        # 1.接收页面中传递的参数
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # 2.实现保存用户信息到user表中
        if User.objects.filter(username=username).exists():
            msg = '账号已存在'
            return render(request, 'backweb/register.html', {'msg': msg})
        if password != password2:
            msg = '密码不一致'
            return render(request, 'backweb/register.html', {'msg': msg})
        password = make_password(password)
        User.objects.create(username=username, password=password)
        return render(request, 'backweb/login.html')


def login(request):
    # 登录
    if request.method == 'GET':
        return render(request, 'backweb/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if check_password(password, user.password):
            # 1.向cookie中保存键值对，键为sessionid
            # 2.向django_session表中存sessionid值
            request.session['user_id'] = user.id
            return redirect('/backweb/article/')
        else:
            msg = '账号或密码错误'
            return render(request, 'backweb/login.html', {'msg': msg})


def logout(request):
    # 退出
    if request.method == 'GET':
        # 1.删除django_session中session_data中的user_id
        # flush() --> 删除
        request.session.flush()
        # 返回登录页面
        return HttpResponseRedirect(reverse('backweb:login'))


def article(request):
    # 文章
    if request.method == 'GET':
        # 获取分页的脚码
        page = int(request.GET.get('page', 1))
        # 使用Paginator实现分页
        # 获取到所有文章
        articles = Article.objects.all()
        pg = Paginator(articles, 5)
        article = pg.page(page)
        return render(request, 'backweb/article.html', {'article': article})



def add_article(request):
    # 增加文章
    if request.method == 'GET':
        column = Column.objects.all()
        return render(request, 'backweb/add_article.html', {'column': column})

    if request.method == 'POST':
        # 获取到页面输入到所有内容
        title = request.POST.get('title')  # 标题
        column = request.POST.get('column')  # 栏目
        describe = request.POST.get('describe')  # 描述
        content = request.POST.get('content')  # 文章内容
        icon = request.FILES.get('icon')  # 图片
        # 保存数据库
        Article.objects.create(title=title,
                               column=column,
                               describe=describe,
                               content=content,
                               icon=icon
                               )

        # 将文章跳转到文章页面
        return HttpResponseRedirect(reverse('backweb:article'))


def update_article(request, id):
    # 修改文章
    if request.method == 'GET':
        articles = Article.objects.filter(pk=id)
        column = Column.objects.all()
        return render(request, 'backweb/update_article.html', {'articles': articles, 'column': column})

    if request.method == 'POST':
        # 获取到页面修改的所有内容
        title = request.POST.get('title')  # 标题
        column = request.POST.get('column')  # 栏目
        describe = request.POST.get('describe')  # 描述
        content = request.POST.get('content')  # 文章内容
        icon = request.FILES.get('icon')  # 图片
        # 保存数据库
        Article.objects.filter(pk=id).update(title=title,
                               column=column,
                               describe=describe,
                               content=content,
                               icon=icon
                               )
        # 返回文章展示页面
        return HttpResponseRedirect(reverse('backweb:article'))


def del_article(request, id):
    # 删除文章
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backweb:article'))


def category(request):
    # 栏目
    if request.method == 'GET':
        column = Column.objects.all()
        return render(request, 'backweb/category.html', {'column': column})

    if request.method == 'POST':
        # 增加栏目
        # 获取到要增加到数据
        # 名字
        column_name = request.POST.get('name')
        # 别名
        c_name = request.POST.get('alias')
        # 描述
        describe = request.POST.get('describe')
        # 保存
        Column.objects.create(column_name=column_name,
                              c_name=c_name,
                              describe=describe)
        # 返回栏目页面
        return HttpResponseRedirect(reverse('backweb:category'))


def update_category(request, id):
    # 更改栏目
    if request.method == 'GET':
        column = Column.objects.filter(pk=id)
        return render(request, 'backweb/update_category.html', {'column': column})

    if request.method == 'POST':
        # 修改栏目
        # 获取到要增加到数据
        # 名字
        column_name = request.POST.get('name')
        # 别名
        c_name = request.POST.get('alias')
        # 描述
        describe = request.POST.get('describe')
        # 保存
        Column.objects.filter(pk=id).update(column_name=column_name,
                              c_name=c_name,
                              describe=describe)
        # 返回栏目页面
        return HttpResponseRedirect(reverse('backweb:category'))


def del_category(request, id):
    # 删除栏目
    if request.method == 'GET':
        Column.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backweb:category'))


def user_modify_the(request, id):
    # 个人信息修改
    if request.method == 'GET':
        # 获取个人信息
        user = User.objects.filter(pk=id)
        return render(request, 'backweb/user_modify_the.html', {'user': user})
    if request.method == 'POST':
        # 获取到修改内容
        # 名字
        username = request.POST.get('username')
        # 工作技能
        job_skills = request.POST.get('job_skills')
        # 自我介绍
        user_introduce = request.POST.get('user_introduce')
        # 职业
        professional = request.POST.get('professional')
        # 邮箱
        email = request.POST.get('email')
        # 微信图片
        wx = request.FILES.get('wx')
        # 头像
        head_portrait = request.FILES.get('head_portrait')
        # 修改信息并保存
        user = User.objects.filter(pk=id).first()
        user.username = username
        user.job_skills = job_skills
        user.user_introduce = user_introduce
        user.wx = wx
        user.head_portrait = head_portrait
        user.professional = professional
        user.email = email
        user.save()
        return HttpResponseRedirect(reverse('web:about'))
