from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

# Create your models here.

class BooksView(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'

class BooksReservedView(ListView):
    model = Book
    template_name = 'books_reserved.html'
    context_object_name = 'books_reserved'

class BookDetailedView(DetailView):
    model = Book
    template_name = 'detail_book.html'
    context_object_name = 'book'