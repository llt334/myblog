from django.db import models


class Category(models.Model):
    name = models.CharField('文章分类', max_length=50)
    description = models.CharField('分类描述', max_length=400)

    class Meta:
        verbose_name = verbose_name_plural = '分类'
        ordering = ['name', ]

    def __str__(self):
        return self.name



