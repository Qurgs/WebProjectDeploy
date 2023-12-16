from rest_framework.viewsets import GenericViewSet
from .serializers import CreateCustomUserSerializer, CustomUserSerializer
from .models import CustomUser
from rest_framework import mixins
from .permissions import IsOwnerOrReadOnly


class CreateCustomUserView(
    mixins.CreateModelMixin,
    GenericViewSet
):
    queryset = CustomUser.objects.all()
    serializer_class = CreateCustomUserSerializer


class CustomUserView(
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = CustomUser
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly]
