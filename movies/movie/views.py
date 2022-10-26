from django.shortcuts import render
from .models import Movie, Director
from .forms import DirectorForm, MovieForm
# Create your views here.


def home(request):
    movie_list = Movie.objects.all()
    directors_list = Director.objects.all()
    context = {
        "movies": movie_list,
        "directors": directors_list
    }
    return render(
        request,
        'index.html',
        context
    )

def add_movie(request):
    form = MovieForm()
    context = {
        'titulo': 'Pelicula',
        'form': form
    }
    return render(
        request,
        'add.html',
        context
    )

def add_director(request):
    form = DirectorForm()
    context = {
        'titulo': 'Director',
        'form': form
    }
    return render(
        request,
        'add.html',
        context
    )
