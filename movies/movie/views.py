from django.shortcuts import render
from .models import Movie, Director
from .forms import MovieForm
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

def add(request):
    form = MovieForm()
    return render(
        request,
        'add.html',
        {'form': form}
    )