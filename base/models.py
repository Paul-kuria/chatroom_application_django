from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

# room is child of a topic
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #the actual user
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # larger than character field.. blank (forms) can be empty
    # participants = store users active in a room
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True) # will always be the initial timestamp.

    class Meta:
        ordering = ['updated', 'created']

    def __str__(self):
        return str(self.name)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Django has a builtin user model
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # one to many relationships. When a room is deleted, delete the messages too.
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50] # Preview of first 50 characters.

