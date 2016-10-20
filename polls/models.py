from django.db import models
import logging

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    guid =  models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    def __str__(self):
        return "title = %s" %self.title

class Filter(models.Model):
    type = models.CharField(max_length=200)
    def __str__(self):
        return "type = %s" %self.type


