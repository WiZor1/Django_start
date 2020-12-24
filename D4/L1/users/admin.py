from django.contrib import admin
from .models import RegularUser
from .forms import RegularUserChangeForm, RegularUserCreationForm

from django.contrib.auth.admin import UserAdmin

# Register your models here.

class RegularUserAdmin(UserAdmin):
    add_form = RegularUserCreationForm
    form = RegularUserChangeForm
    model = RegularUser
    list_display = ['username', 'sex', 'postal_code', 'email']

admin.site.register(RegularUser, RegularUserAdmin)