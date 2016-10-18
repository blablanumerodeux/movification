from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Feed
from .forms import NameForm
import logging

def feed(request):
    template = loader.get_template('index.html')
    context = {
        'listMovies': Feed.listMovies
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
            listFilters.append(form.cleaned_data.movie_type)
            #need to fetch other values from database for the same user
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


