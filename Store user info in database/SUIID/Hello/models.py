from django.db import models

# Create your models here.
class User_login(models.Model):
    First_Name = models.CharField(max_length=128)
    Last_Name = models.CharField(max_length=128)
    Email = models.EmailField(max_length=264,unique=True)




