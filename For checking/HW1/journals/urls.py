from django.urls import path
from .views import JournalsView, JournalsReservedView, JournalDetailedView

urlpatterns = [
    path('', JournalsView.as_view(), name='journals'),
    path('journals_reserved/', JournalsReservedView.as_view(), name='journals_reserved'),
    path('journal/<int:pk>/', JournalDetailedView.as_view(), name='journal_detailed'),
]