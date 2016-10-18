from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.feed, name='feed'),
    url(r'^movie_type/$', views.movie_type, name='form'),
    url(r'^filter_added/$', views.filter_added, name='filter_added'),
]

