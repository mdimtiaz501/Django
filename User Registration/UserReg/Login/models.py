from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='Login/profile_pictures',blank=True)

    def __str__(self):
        return self.user.username






