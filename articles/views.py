from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):
    queryset = Article.objects.filter(status='publish')
    context_object_name = 'articles'
    template_name = 'articles/articles_list.html'


class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = ''