from django.db import models

# Create your models here.


class User(models.Model):
    # 用户
    # 名字
    username = models.CharField(max_length=10, unique=True)
    # 密码
    password = models.CharField(max_length=150, null=False)
    # 时间
    crate_time = models.DateTimeField(auto_now_add=True)
    # 职业
    professional = models.CharField(max_length=12, null=True)
    # 邮箱
    email = models.CharField(max_length=17, null=True)
    # 微信
    wx = models.ImageField(upload_to='user', null=True)
    # 头像
    head_portrait = models.ImageField(upload_to='user', null=True)
    # 工作技能
    job_skills = models.TextField(null=True)
    # 自我介绍
    user_introduce = models.TextField(null=True)
    # 职业
    professional = models.TextField(null=True)

    class Meta:
        db_table = 'user'


class UserToken(models.Model):
    # 这个是个存token值的表
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=20)

    class Meta:
        db_table = 'user_token'


class Column(models.Model):  # 栏目
    # 栏目名字
    column_name = models.CharField(max_length=30, null=False)
    # 栏目别名
    c_name = models.CharField(max_length=30, null=False)
    # 描述
    describe = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'column'


class Article(models.Model):   # 文章
    # 标题
    title = models.CharField(max_length=30, null=False)
    # 栏目
    column = models.CharField(max_length=20, null=True)
    # 描述
    describe = models.CharField(max_length=100, null=True, default='作者很懒，没有写描述')
    # 文章内容
    content = models.TextField(null=False)
    # 文章图片
    icon = models.ImageField(upload_to='article', null=True)
    # 创建时的时间时间
    time = models.DateTimeField(auto_now_add=True)
    # 修改时的时间
    g_time = models.DateTimeField(auto_now=True)
    # 一对多的关联，文章关联栏目foreignkey定义在多的一方
    c = models.ForeignKey(Column, null=True, on_delete=models.CASCADE)
    class Meta:
        db_table = 'article'


