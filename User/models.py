from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    favorite_movie = models.ManyToManyField(
        'Cinema.Movie',
        related_name='user_favorite_movie',
    )
    avatar = models.ImageField(
        upload_to='images/user_images/',
        default='images/user_image.jpg',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username
