from django.db import models
from django.contrib.auth.models import User

class Chatroom(models.Model):
        name = models.CharField(max_length=200)
        slug = models.SlugField(max_length=100)
        
        
class ChatMessage(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        room = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
        message_content = models.TextField()
        date = models.DateTimeField(auto_now=True)

        class Meta:
            ordering= ('date',)

        def __str__(self):
            return self.message_content



        
