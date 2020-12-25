from .models import Store

# Заготовки интерфейса пользовательской модели
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class StoreCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Store
        fields = ('username', 'email', 'inn', 'year_open')



class StoreChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Store
        fields = ('username', 'email', 'inn', 'year_open')