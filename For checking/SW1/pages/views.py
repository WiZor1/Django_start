from django.shortcuts import render
from django.views.generic import TemplateView

# Create your models here.

class HomeView(TemplateView):
    template_name = 'home.html'