# Generated by Django 5.0 on 2023-12-16 19:03

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='birth_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(1000, 1, 1)), django.core.validators.MaxValueValidator(datetime.date(2023, 12, 16))]),
        ),
    ]