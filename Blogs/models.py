from django.db import models

# Create your models here.

class create_profile(models.Model):
    user_name = models.CharField(max_length=120)
    email= models.EmailField(max_length=120,unique=True,primary_key=True)
    password = models.CharField(max_length=120)