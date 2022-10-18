from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    imdb = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " " +self.last_name