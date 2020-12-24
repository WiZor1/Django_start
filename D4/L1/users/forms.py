from .models import RegularUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegularUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = RegularUser
        fields = UserCreationForm.Meta.fields + ('phone_number', 'postal_code', 'age', 'sex',)

class RegularUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        model = RegularUser
        fields = UserCreationForm.Meta.fields + ('phone_number', 'postal_code', 'age', 'sex',)
