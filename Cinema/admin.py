from django.contrib import admin

from .models import *


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class DirectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'surname')}


class ActorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'surname')}


class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Country, CountryAdmin)


