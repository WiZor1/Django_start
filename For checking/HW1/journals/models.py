from django.db import models

# Create your models here.

class Journal(models.Model):
    title = models.CharField(max_length=250)
    editor = models.CharField(max_length=100)
    pages_count = models.IntegerField()

    def __str__(self):
        return self.title