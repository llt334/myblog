# Generated by Django 2.2.16 on 2020-10-01 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='文章分类')),
                ('description', models.CharField(max_length=240, verbose_name='分类描述')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('description', models.CharField(max_length=500, verbose_name='概述')),
                ('photo', models.ImageField(blank=True, upload_to='images/article/%Y/%m/%d', verbose_name='博文图片')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('status', models.CharField(choices=[('publish', '发布'), ('draft', '草稿')], max_length=10, verbose_name='是否发布')),
                ('is_top', models.BooleanField(default=False, verbose_name='置顶')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('published', models.DateTimeField(blank=True, verbose_name='发布时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读数量')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='articles.Category', verbose_name='分类')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='标签')),
            ],
        ),
    ]