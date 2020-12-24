from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegularUserCreationForm

# Create your views here.

class SignUpView(CreateView):
    form_class = RegularUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy("login")