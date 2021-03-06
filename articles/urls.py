from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView
)


app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='all'),
    path('<slug:slug>', ArticleDetailView.as_view(), name='detail'),
]
