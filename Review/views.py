from .serializers import *
from .models import *
from rest_framework import viewsets
from .permissions import IsOwnerOrAdminOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly, IsAuthenticatedOrReadOnly]

