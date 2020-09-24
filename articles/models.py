from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField('文章分类', max_length=50)
    description = models.CharField('分类描述', max_length=400)

    class Meta:
        verbose_name = verbose_name_plural = '分类'
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS = {
        ('draft', '草稿'),
        ('publish', '发布'),
    }
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE, related_name='articles')
    title = models.CharField('标题', max_length=100)
    description = models.CharField('概述', max_length=500)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE, related_name='articles')
    content = models.TextField('文章内容')
    tags = TaggableManager(verbose_name='标签', blank=True)
    status = models.CharField('是否发布', choices=STATUS)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    published = models.DateTimeField('发布时间', blank=True)
    updated = models.DateTimeField('更新时间', auto_now=True)
    views = models.PositiveIntegerField('阅读数量', default=0)

    def __str__(self):
        return self.title


