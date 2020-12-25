from django.urls import path 
from .views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleCreateNew

urlpatterns = [
    path('', ArticleListView.as_view(), name='list_articles'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail_article'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='update_article'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete_article'),
    path('new/', ArticleCreateNew.as_view(), name='new_article'),
]