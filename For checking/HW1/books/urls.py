from django.urls import path
from .views import BooksView, BooksReservedView, BookDetailedView

urlpatterns = [
    path('', BooksView.as_view(), name='books'),
    path('books_reserved/', BooksReservedView.as_view(), name='books_reserved'),
    path('book/<int:pk>', BookDetailedView.as_view(), name='book_detailed')
]