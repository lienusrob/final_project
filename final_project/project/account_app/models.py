
from django.db import models
from django.contrib.auth.models import User 
from django.dispatch import receiver 
from django.db.models.signals import post_save 
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)