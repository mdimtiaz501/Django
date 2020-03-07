from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=256)
    Faculty = models.CharField(max_length=256)
    Department = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    Department = models.ForeignKey(University,on_delete=models.CASCADE,related_name='stdnts')
    #should be written university
    def __str__(self):
        return self.name
