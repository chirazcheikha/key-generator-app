from django.db import models
from django.contrib.auth.models import User



# key object to use in the serializer as a model
class Key(models.Model):
    key_name = models.CharField(max_length=100,null=True,blank=True)
    key_description = models.CharField(max_length=200,null=True,blank=True)
    key = models.CharField(max_length=15,null=True,blank=True)
    date= models.DateTimeField(auto_now_add=True)
    