from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    msg = models.TextField()
    
class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)