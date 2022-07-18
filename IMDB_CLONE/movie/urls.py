from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.MovieList.as_view(),name="MovieList"),
    path('action/',views.ActionGenre.as_view(),name="ActionGenre"),
    path('comedy/',views.ComedyGenre.as_view(),name="ComedyGenre"),
    path('scifi/',views.ScifiGenre.as_view(),name="ScifiGenre"),
    path('drama/',views.DramaGenre.as_view(), name="DramaGenre"),
    path('<pk>/',views.MovieDetail.as_view(),name="MovieDetail"),
    path('new/recent/',views.RecentlyMovies.as_view(),name="RecentMovie"),
]