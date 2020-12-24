from django.contrib.auth.models import AbstractUser
from django.db import models


class RegularUser(AbstractUser):
    phone_number = models.TextField(null=False, blank=False) # номер телефона пользователя
    postal_code = models.TextField(null=False, blank=False) # почтовый индекс пользователя
    age = models.PositiveIntegerField(null=True, blank=True) # возраст пользователя
    sex = models.BooleanField(null=True, blank=True) # пол пользователя (True - Женский, False - мужской)