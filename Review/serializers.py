from rest_framework import serializers
from .models import *


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.CharField()

    class Meta:
        model = Review
        fields = '__all__'
