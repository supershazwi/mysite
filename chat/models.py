from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    sender = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.text