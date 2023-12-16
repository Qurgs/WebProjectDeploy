from rest_framework import serializers
from .models import CustomUser
from Cinema.models import Movie


class CreateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'birth_date', 'avatar']


class CustomUserSerializer(serializers.ModelSerializer):
    favorite_movie = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        many=True,
        required=False
    )
    username = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'birth_date', 'avatar', 'favorite_movie']
