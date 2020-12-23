from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Journal

# Create your models here.

class JournalsView(ListView):
    model = Journal
    template_name = 'journals.html'
    context_object_name = 'journals'

class JournalsReservedView(ListView):
    model = Journal
    template_name = 'journals_reserved.html'
    context_object_name = 'journals_reserved'

class JournalDetailedView(DetailView):
    model = Journal
    template_name = 'detail_journal.html'
    context_object_name = 'journal'