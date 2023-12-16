from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework import routers
from .views import CreateCustomUserView, CustomUserView

router = routers.DefaultRouter()
router.register(r'create', CreateCustomUserView, basename='user_create')
router.register(r'info', CustomUserView, basename='user_create')

urlpatterns = [
    path('user/', include(router.urls)),
    path('user/token/create/', TokenCreateView.as_view(), name='token_create'),
    path('user/token/destroy', TokenDestroyView.as_view(), name='token_destroy1')
]
