import random

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=200)
    #secret = models.CharField(max_length=200)
    description = models.TextField()
    download = models.FileField()

    def __str__(self):
        return self.name

    @property
    def random_screenshot(self):
        screens = list(self.screenshot_set.all())
        if not screens:
            return None
        return random.choice(screens)


class Score(models.Model):
    score = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    started_at = models.DateTimeField('Started at: ')
    ended_at = models.DateTimeField('Ended at: ')
    system_info = models.TextField(max_length=500)

    def __str__(self):
        return "{}, {}, {}".format(self.game, self.user, self.score)


class Screenshot(models.Model):
    image = models.ImageField()
    caption = models.TextField()
    game = models.ForeignKey(Game)

    def __str__(self):
        return "{}, {}".format(self.game, self.caption)
