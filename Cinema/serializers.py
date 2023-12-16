from rest_framework import serializers
from .models import *
from Review.serializers import ReviewSerializer


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)
    country = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = [
            'title', 'genre', 'country', 'publication_year',
            'age_rating', 'poster', 'tagline'
        ]


class MovieDetailSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)
    main_actors = serializers.StringRelatedField(many=True)
    country = serializers.StringRelatedField()
    director = serializers.StringRelatedField()
    reviews = ReviewSerializer(
        many=True,
        source='review_movie',
        required=False,
        allow_null=True
    )

    class Meta:
        model = Movie
        fields = '__all__'
