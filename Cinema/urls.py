from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieView, basename='movies')
router.register(r'genres', views.GenreView, basename='genres')
router.register(r'actors', views.ActorView, basename='actors')
router.register(r'directors', views.DirectorView, basename='directors')
router.register(r'countries', views.CountryView, basename='countries')

urlpatterns = [
    path('', include(router.urls)),
]
