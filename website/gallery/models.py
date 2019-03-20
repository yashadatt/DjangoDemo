from django.db import models

class Photo(models.Model):
    photo = models.ImageField()

class Video(models.Model):
    video = models.CharField(max_length=1000)
