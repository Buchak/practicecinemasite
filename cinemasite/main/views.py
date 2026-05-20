from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from . import models, forms


def categories_list(request: HttpRequest) -> HttpResponse:
    context = {
        'categories': models.Category.objects.all()
    }
    return render(request, 'main/categories-list.html', context=context)


def category_detail(request: HttpRequest, category_slug) -> HttpResponse:
    category = get_object_or_404(
        models.Category.objects.prefetch_related('movies'),
        slug=category_slug)

    context = {
        'category': category
    }
    return render(request, 'main/category-detail.html', context=context)


def movies_list(request: HttpRequest) -> HttpResponse:
    context = {
        'movies': models.Movie.objects.all(),
    }
    return render(request, 'main/movies-list.html', context=context)


def movie_detail(request: HttpRequest, movie_slug) -> HttpResponse:
    movie = get_object_or_404(models.Movie.objects.prefetch_related('actors'), slug=movie_slug)
    context = {
        'movie': movie,
    }
    return render(request, 'main/movie-detail.html', context=context)


def actors_list(request: HttpRequest) -> HttpRequest:
    context = {
        'actors': models.Actor.objects.all(),
    }
    return render(request, 'main/actors-list.html', context=context)


def actor_detail(request: HttpRequest, actor_slug) -> HttpResponse:
    actor = get_object_or_404(models.Actor.objects.prefetch_related('movies'), slug=actor_slug)
    context = {
        'actor': actor,
    }
    return render(request, 'main/actor-detail.html', context=context)


def create_movie(request: HttpRequest) -> HttpResponse:
    context = {
        'form': forms.MovieForm(),
    }
    return render(request, 'main/create-movie.html', context=context)
