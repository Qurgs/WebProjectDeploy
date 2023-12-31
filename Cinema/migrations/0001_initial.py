# Generated by Django 4.1.7 on 2023-12-15 16:38

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contributor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                ("surname", models.CharField(max_length=255, verbose_name="Surname")),
                (
                    "birth_date",
                    models.DateField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                datetime.date(1000, 1, 1)
                            ),
                            django.core.validators.MaxValueValidator(
                                datetime.date(2023, 12, 15)
                            ),
                        ]
                    ),
                ),
                ("height", models.FloatField(verbose_name="Height in meters")),
                ("slug", models.SlugField(unique=True, verbose_name="Slug")),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, unique=True, verbose_name="Name"),
                ),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="Slug"),
                ),
            ],
            options={
                "verbose_name": "Country",
                "verbose_name_plural": "Countries",
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                ("description", models.TextField(verbose_name="Description")),
                ("slug", models.SlugField(unique=True, verbose_name="slug")),
            ],
            options={
                "verbose_name": "Genre",
                "verbose_name_plural": "Genres",
            },
        ),
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "contributor_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="Cinema.contributor",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        upload_to="images/actors_images/", verbose_name="Photo"
                    ),
                ),
            ],
            options={
                "verbose_name": "Actor",
                "verbose_name_plural": "Actors",
            },
            bases=("Cinema.contributor",),
        ),
        migrations.CreateModel(
            name="Director",
            fields=[
                (
                    "contributor_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="Cinema.contributor",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        upload_to="images/directors_images/", verbose_name="Photo"
                    ),
                ),
            ],
            options={
                "verbose_name": "Director",
                "verbose_name_plural": "Directors",
            },
            bases=("Cinema.contributor",),
        ),
        migrations.AddField(
            model_name="contributor",
            name="birth_country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Cinema.country",
                verbose_name="Birth country",
            ),
        ),
        migrations.AddField(
            model_name="contributor",
            name="genres",
            field=models.ManyToManyField(to="Cinema.genre", verbose_name="Genres"),
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "publication_year",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1000),
                            django.core.validators.MaxValueValidator(2023),
                        ],
                        verbose_name="Publication year",
                    ),
                ),
                (
                    "age_rating",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                        verbose_name="Age rating",
                    ),
                ),
                ("tagline", models.CharField(max_length=255, verbose_name="Tagline")),
                (
                    "poster",
                    models.ImageField(
                        upload_to="images/movie_images/", verbose_name="Poster image"
                    ),
                ),
                ("slug", models.SlugField(unique=True, verbose_name="Slug")),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Cinema.country",
                        verbose_name="Country",
                    ),
                ),
                (
                    "genre",
                    models.ManyToManyField(
                        related_name="movie_genre",
                        to="Cinema.genre",
                        verbose_name="Genre",
                    ),
                ),
                (
                    "director",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Cinema.director",
                        verbose_name="Director",
                    ),
                ),
                (
                    "main_actors",
                    models.ManyToManyField(
                        related_name="movie_actors",
                        to="Cinema.actor",
                        verbose_name="Actors",
                    ),
                ),
            ],
            options={
                "verbose_name": "Movie",
                "verbose_name_plural": "Movies",
            },
        ),
    ]
