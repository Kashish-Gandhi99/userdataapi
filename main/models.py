from django.db import models
import datetime

# Create your models here.

class User(models.Model):
   name = models.CharField(max_length=32)
   timezone = models.CharField(max_length=32)

class Useractivity(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE,related_name='activity')
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()

    class Meta:
        ordering = ['id']
   
    def __str__(self):
      return '%s %s' % (" 'Starttime' : " + self.starttime.strftime("%d %B, %Y, %H:%M:%S%p"), "'Endtime' : " + self.endtime.strftime("%d %B, %Y, %H:%M:%S%p")) +" "
       