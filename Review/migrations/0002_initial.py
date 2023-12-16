# Generated by Django 4.1.7 on 2023-12-15 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Cinema", "0001_initial"),
        ("Review", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="review_author",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Author",
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="review_movie",
                to="Cinema.movie",
                verbose_name="Movie",
            ),
        ),
    ]
