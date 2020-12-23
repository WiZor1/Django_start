from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail_post.html'
    context_object_name = 'post'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'new_post.hmtl'
    fields = '__all__'