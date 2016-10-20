from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Filter
from .models import Movie
from .forms import NameForm
import feedparser
import omdb
import logging

def feed(request):
    template = loader.get_template('index.html')

    typesFiltered = Filter.objects.values_list('type', flat=True)
    print("list of the types filtered : ")
    print(typesFiltered)

    #we parse the imdb rss feed in order to have a list of DVD Release
    #this is an example of source where we can find the info
    d = feedparser.parse('http://rss.imdb.com/list/ls016522954/')
    entries = d.entries
    listMovies = list()
    for post in entries:
        guidFetched=post.guid.split('/')[-2]
        #we fetch the type on omdb with the imdbid
        typeFetched = omdb.imdbid(guidFetched).genre.replace(" ", "").split(',')
        print("typeFetched = ")
        print(typeFetched)
        #if the type is not filtered then we keep it 
        if not set(typeFetched) & set(typesFiltered): 
            listMovies.append(Movie(title=post.title, guid=guidFetched,type = typeFetched))

    context = {
        'listMovies': listMovies,
        'listTypesFiltered': typesFiltered 
    }
    return HttpResponse(template.render(context, request))


def movie_type(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data)
            listFilters = list()
            f = Filter(type=form.cleaned_data['movie_type'])
            listFilters.append(f)
            f.save()
            print(listFilters)
            # redirect to a new URL:
            return HttpResponseRedirect('/polls/filter_added')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def filter_added(request):
    template = loader.get_template('filter_added.html')
    context = {
        'listMovies': 'toto'
    }
    return HttpResponse(template.render(context, request))



