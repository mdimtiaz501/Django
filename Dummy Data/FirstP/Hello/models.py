from django.db import models

# Create your models here.
class Subject(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey('Subject', on_delete=models.PROTECT)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name        #eta return hoye ForeignKey te boshe jabe

class AccessRecord(models.Model):
    name = models.ForeignKey('Webpage', on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date)





