from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('文章分类', max_length=50)
    description = models.CharField('分类描述', max_length=400)

    class Meta:
        verbose_name = verbose_name_plural = '分类'
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE, related_name='articles')
    title = models.CharField('标题', max_length=100)
    description = models.CharField('概述', max_length=500)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE, related_name='articles')
