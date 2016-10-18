from django.db import models
import feedparser
import logging
import omdb

# Create your models here.

class Movie(models.Model):
    title = models.TextField()
    guid =  models.TextField()
    type = models.TextField()
    


class Filter(models.Model):
    type = models.TextField()



class Feed(models.Model):
    d = feedparser.parse('http://rss.imdb.com/list/ls016522954/')
    title = d.feed.title
    entries = d.entries
    listMovies = list()
    for post in entries:
        guidFetched=post.guid.split('/')[-2]
        typeFetched = omdb.imdbid(guidFetched).genre
        typesFiltered = Filter.objects.values_list('type')
        print(typesFiltered)
        if typeFetched in typesFiltered: 
            listMovies.append(Movie(title=post.title, guid=guidFetched,type = typeFetched))
       


