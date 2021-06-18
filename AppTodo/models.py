from django.db import models

# Create your models here.
class TodoItem(models.Model):
    context = models.TextField()