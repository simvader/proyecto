from django.contrib import admin
from .models import Movie, Director, Actor

# Register your models here.
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)