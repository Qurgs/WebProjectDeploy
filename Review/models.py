from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
    text = models.TextField(verbose_name='Text')
    author = models.ForeignKey(
        'User.CustomUser',
        verbose_name='Author',
        on_delete=models.CASCADE,
        related_name='review_author'
    )
    movie = models.ForeignKey(
        'Cinema.Movie',
        verbose_name='Movie',
        on_delete=models.CASCADE,
        related_name='review_movie',
    )
    rating = models.IntegerField(
        verbose_name='Rating',
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    def __str__(self):
        return self.text
