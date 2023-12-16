from django_filters import rest_framework as filters
from .models import *


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class MovieFilter(filters.FilterSet):
    genre = CharFilterInFilter(field_name='genre__slug', lookup_expr='in')
    publication_year = filters.RangeFilter(field_name='publication_year', lookup_expr='in')
    country = CharFilterInFilter(field_name='country__slug', lookup_expr='in')
    director = CharFilterInFilter(field_name='director__slug', lookup_expr='in')

    class Meta:
        model = Movie
        fields = ['title', 'publication_year']
