from django.db import models

# Create your models here.
class student(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length = 30)
    sclass = models.IntegerField()
    scity = models.CharField(max_length = 30)
