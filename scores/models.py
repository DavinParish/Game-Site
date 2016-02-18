from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=200)
    #secret = models.CharField(max_length=200)
    description = models.TextField()
    download = models.FileField()


class Score(models.Model):
    score = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    started_at = models.DateTimeField('Started at: ')
    ended_at = models.DateTimeField('Ended at: ')
    system_info = models.TextField(max_length=500)


class Screenshot(models.Model):

    image = models.ImageField()
    caption = models.TextField()
    game = models.ForeignKey(Game)