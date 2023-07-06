from django.db import models

# Create your models here.

class Event(models.Model):
    creator_id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    categories = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)

class Participants(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()

    Event=models.ForeignKey(Event, on_delete=models.CASCADE)
