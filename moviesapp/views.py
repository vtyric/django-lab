from django.shortcuts import render

from .models import Movie, Actor, Genre, Category


def home(request):
    return render(request, 'moviesapp/home.html')


def movie_list(request):
    """Вывод всех фильмов"""
    movies = Movie.objects.all()
    return render(request, 'moviesapp/movie_list.html', {'movies': movies})


def actor_list(request):
    """Вывод всех актеров/режиссеров"""
    actors = Actor.objects.all()
    return render(request, 'moviesapp/actor_list.html', {'actors': actors})


def genre_list(request):
    """Вывод всех жанров"""
    genres = Genre.objects.all()
    return render(request, 'moviesapp/genre_list.html', {'genres': genres})


def category_list(request):
    """Вывод всех категорий"""
    categories = Category.objects.all()
    return render(request, 'moviesapp/category_list.html', {'categories': categories})
