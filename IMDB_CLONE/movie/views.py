from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie
# Home Page
class MovieList(ListView):
    model=Movie
    template_name="movie/movie_list.html"
    context_object_name="movies"

    def get_queryset(self):
        return Movie.objects.all().order_by('?')

# Action Movies
class ActionGenre(ListView):
    model=Movie
    template_name="movie/movie_genre.html"
    context_object_name="movies"

    def get_queryset(self):
        return Movie.objects.filter(genre="A").order_by('-id')

# Comdey Movies
class ComedyGenre(ListView):
    model=Movie
    template_name="movie/movie_genre.html"
    context_object_name="movies"

    def get_queryset(self):
        return Movie.objects.filter(genre="C").order_by('-id')

# Drama Movies
class DramaGenre(ListView):
    model=Movie
    template_name="movie/movie_genre.html"
    context_object_name="movies"

    def get_queryset(self):
        return Movie.objects.filter(genre="D").order_by('-id')

# Sci-fi
class ScifiGenre(ListView):
    model=Movie
    template_name="movie/movie_genre.html"
    context_object_name="movies"

    def get_queryset(self):
        return Movie.objects.filter(genre="S").order_by('-id')

class MovieDetail(DetailView):
    model=Movie
    template_name="movie/movie_detail.html"
    context_object_name="movie"

class RecentlyMovies(ListView):
    model=Movie
    template_name="movie/movie_genre.html"
    context_object_name="movies"

    def get_queryset(self):
        return Movie.objects.all().order_by('-id')[:9]

