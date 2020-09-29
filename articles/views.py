from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Article


class ArticleListView(ListView):
    queryset = Article.objects.filter(status='publish')
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'




