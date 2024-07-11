from django.urls import path
from .views import *

app_name = 'articles'

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='list'),
    path('articles/diet/', diet_view, name='diet-detail'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
]
