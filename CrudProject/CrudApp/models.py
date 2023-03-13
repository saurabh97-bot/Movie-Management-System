import datetime

from django.db import models
from django.utils import timezone

class Movie(models.Model):
    name = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='movieimages')
    description = models.TextField()
    released_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Slides(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name


