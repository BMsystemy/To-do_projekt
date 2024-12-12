from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)  # Tytuł zadania
    completed = models.BooleanField(default=False)  # Status ukończenia
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Umożliwiamy wartość NULL
    created_at = models.DateTimeField(auto_now_add=True)  # Data utworzenia
    due_date = models.DateTimeField(null=True, blank=True)  # Data i czas wykonania zadania

    def __str__(self):
        return self.title
