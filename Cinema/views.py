from .serializers import *
from .models import *
from rest_framework import viewsets, permissions, filters
from .permissions import IsAdminOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .service import MovieFilter
from django.shortcuts import render


def welcome(request):
    return render(request, 'cinemago/index.html')

def typing_game(reqeust):
    return render(reqeust, 'cinemago/typing_game.html')


class MoviePagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 100


class GeneralView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'


class CountryView(GeneralView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class DirectorView(GeneralView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class ActorView(GeneralView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreView(GeneralView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieView(GeneralView):
    queryset = Movie.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_class = MovieFilter
    pagination_class = MoviePagination

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        return MovieDetailSerializer

