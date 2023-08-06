from django.db import models


class Chatroom(models.Model):
        name = models.CharField(max_length=200)
        slug = models.SlugField(max_length=100)
