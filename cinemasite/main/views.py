from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from . import models


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


def movie_detail(request: HttpRequest, movie_slug) -> HttpResponse:
    movie = get_object_or_404(models.Movie, slug=movie_slug)
    context = {
        'movie': movie,
    }
    return render(request, 'main/movie-detail.html', context=context)
