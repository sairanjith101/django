from django.db import models

# Create your models here.

class Student(models.Model):
    studno = models.IntegerField()
    studname = models.CharField(max_length = 20)
    studclass = models.IntegerField()
    studaddress = models.CharField(max_length = 100)

def __str__(self):
    return 'Student details are shared'