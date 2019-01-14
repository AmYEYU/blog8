from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from backweb.models import Article, Column, User


def index(request):
    # 首页
    if request.method == 'GET':
        # 文章
        article = Article.objects.all()
        # 栏目
        column = Column.objects.all()
        # 用户
        user = User.objects.all()

        return render(request, 'web/index.html', {'article': article, 'column': column, 'user': user})


def about(request):
    # 关于我
    if request.method == 'GET':
        user = User.objects.all()
        return render(request, 'web/about.html', {'user': user})


def list(request):
    # 博客文章
    if request.method == 'GET':
        user = User.objects.all()
        article = Article.objects.all()
        column = Column.objects.all()
        return render(request, 'web/list.html', {'user': user, 'article': article, 'column': column})


def info(request, id):
    # 文章详情
    if request.method == 'GET':
        article = Article.objects.filter(pk=id)
        return render(request, 'web/info.html', {'article': article})


