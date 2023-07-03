from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        default=timezone.now)  # Fecha de creación
    # Última fecha de actualización
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
