from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(verbose_name='用户名称',max_length=32)
    password=models.CharField(verbose_name='用户密码',max_length=32)
    role=models.OneToOneField(verbose_name='用户权限',to='Role')
class Role(models.Model):
    name=models.CharField(verbose_name='权限名称',max_length=32)
    role_choice=((1,'管理员'),(2,'普通用户'))
    type=models.IntegerField(verbose_name='权限等级',choices=role_choice)
class Article(models.Model):
    title=models.CharField(verbose_name='文章标题',max_length=32)
    content=models.TextField(verbose_name='文章详细')
    create_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    tag=models.ForeignKey(verbose_name='文章所属小类型',to='Tag',related_name='article')
class Category(models.Model):
    title=models.CharField(verbose_name='文章大分类名称',max_length=32)
    def __str__(self):
        return self.title
class Tag(models.Model):
    title=models.CharField(verbose_name='文章小分类名称',max_length=32)
    cate=models.ForeignKey(verbose_name='文章小分类关联的大分类',to='Category',related_name='tag')
