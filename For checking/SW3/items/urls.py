from django.urls import path 
from .views import ItemListView, ItemDetailView, ItemUpdateView, ItemDeleteView, ItemCreateNew

urlpatterns = [
    path('', ItemListView.as_view(), name='list_items'),
    path('<int:pk>/detail/', ItemDetailView.as_view(), name='detail_item'),
    path('<int:pk>/edit/', ItemUpdateView.as_view(), name='update_item'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='delete_item'),
    path('new/', ItemCreateNew.as_view(), name='new_item'),
]