from django.db import models

# Create your models here.
#Eric - This is where database wrappers go

class User(models.Model):
    name = models.CharField(max_length=100)
    dateOfSignup = models.dateTimeField('date of signup')
    age = models.IntegerField(default=0)
    personId = personId + 1

class Event(models.Model):
    creator = models.ForeignKey(User)
    eventId = eventId + 1
    name = models.CharField(max_length=1000)
