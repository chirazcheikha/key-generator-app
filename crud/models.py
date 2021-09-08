from django.db import models
from django.contrib.auth.models import User


class Key(models.Model):
    key_name = models.CharField(max_length=100)
    key_description = models.CharField(max_length=200)
    key = models.CharField(max_length=200)
    date= models.DateTimeField(auto_now_add=True)
    