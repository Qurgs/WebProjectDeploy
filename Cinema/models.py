from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Country(models.Model):
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
    name = models.CharField(verbose_name='Name', max_length=255, unique=True)
    slug = models.SlugField(verbose_name='Slug', max_length=255, unique=True)

    def __str__(self):
        return self.name


class Contributor(models.Model):
    name = models.CharField(verbose_name='Name', max_length=255)
    surname = models.CharField(verbose_name='Surname', max_length=255)
    birth_date = models.DateField(
        validators=[
            MinValueValidator(timezone.datetime(1000, 1, 1).date()),
            MaxValueValidator(timezone.now().date()),
        ]
    )
    genres = models.ManyToManyField('Genre', verbose_name='Genres')
    birth_country = models.ForeignKey(
        Country,
        verbose_name='Birth country',
        on_delete=models.CASCADE
    )
    height = models.FloatField(verbose_name='Height in meters')
    slug = models.SlugField(verbose_name='Slug', unique=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Actor(Contributor):
    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'
    photo = models.ImageField(verbose_name='Photo', upload_to='images/actors_images/')


class Director(Contributor):
    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'
    photo = models.ImageField(verbose_name='Photo', upload_to='images/directors_images/')


class Genre(models.Model):
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
    name = models.CharField(verbose_name='Name', max_length=255)
    description = models.TextField(verbose_name='Description')
    slug = models.SlugField(verbose_name='slug', unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    title = models.CharField(
        verbose_name='Title',
        max_length=255
    )
    description = models.TextField(verbose_name='Description')
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Genre',
        related_name='movie_genre'
    )
    publication_year = models.PositiveSmallIntegerField(
        verbose_name='Publication year',
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(timezone.now().year),
        ]
    )
    age_rating = models.PositiveSmallIntegerField(
        verbose_name='Age rating',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ]
    )
    tagline = models.CharField(
        verbose_name='Tagline',
        max_length=255
    )
    poster = models.ImageField(
        verbose_name='Poster image',
        upload_to='images/movie_images/'
    )
    main_actors = models.ManyToManyField(
        Actor,
        verbose_name='Actors',
        related_name='movie_actors'
    )
    country = models.ForeignKey(
        Country,
        verbose_name='Country',
        on_delete=models.CASCADE
    )
    director = models.ForeignKey(
        Director,
        verbose_name='Director',
        on_delete=models.CASCADE
    )
    slug = models.SlugField(
        verbose_name='Slug',
        unique=True
    )

    def __str__(self):
        return self.title
