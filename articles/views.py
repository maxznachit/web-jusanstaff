from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    ordering = ['-id']
    paginate_by = 10  # беттерге бөлу


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'


def diet_view(request):
    return render(request, "articles/diet_view.html")
