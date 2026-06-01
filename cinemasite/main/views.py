from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from . import models, forms


# def categories_list(request: HttpRequest) -> HttpResponse:
#     context = {
#         'categories': models.Category.objects.all()
#     }
#     return render(request, 'main/categories-list.html', context=context)


class CategoryListView(ListView):
    template_name = 'main/categories-list.html'
    model = models.Category
    context_object_name = 'categories'


# def category_detail(request: HttpRequest, category_slug) -> HttpResponse:
#     category = get_object_or_404(
#         models.Category.objects.prefetch_related('movies'),
#         slug=category_slug)
#
#     context = {
#         'category': category
#     }
#     return render(request, 'main/category-detail.html', context=context)


class CategoryDetailView(DetailView):
    template_name = 'main/category-detail.html'
    model = models.Category
    context_object_name = 'category'


# def movies_list(request: HttpRequest) -> HttpResponse:
#     context = {
#         'movies': models.Movie.objects.all(),
#     }
#     return render(request, 'main/movies-list.html', context=context)


class MovieListView(ListView):
    template_name = 'main/movies-list.html'
    model = models.Movie
    context_object_name = 'movies'


# def movie_detail(request: HttpRequest, movie_slug) -> HttpResponse:
#     movie = get_object_or_404(models.Movie.objects.prefetch_related('actors'), slug=movie_slug)
#     context = {
#         'movie': movie,
#     }
#     return render(request, 'main/movie-detail.html', context=context)


class MovieDetailView(DetailView):
    template_name = 'main/movie-detail.html'
    model = models.Movie
    context_object_name = 'movie'
    slug_url_kwarg = 'movie_slug'


# def create_movie(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         form = forms.MovieForm(request.POST, request.FILES)
#         if form.is_valid():
#             models.Movie.objects.create(**form.cleaned_data)
#     else:
#         form = forms.MovieForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'main/create-movie.html', context=context)


class MovieCreateView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'form': forms.MovieForm(),
        }
        return render(request, 'main/create-movie.html', context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = forms.MovieForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('main:movie-detail', movie_slug=form.cleaned_data['movie_slug'])

        context = {
            'form': form,
        }
        return render(request, 'main/create-movie.html', context=context)


# def actors_list(request: HttpRequest) -> HttpRequest:
#     context = {
#         'actors': models.Actor.objects.all(),
#     }
#     return render(request, 'main/actors-list.html', context=context)


class ActorListView(ListView):
    template_name = 'main/actors-list.html'
    model = models.Actor
    context_object_name = 'actors'


# def actor_detail(request: HttpRequest, actor_slug) -> HttpResponse:
#     actor = get_object_or_404(models.Actor.objects.prefetch_related('movies'), slug=actor_slug)
#     context = {
#         'actor': actor,
#     }
#     return render(request, 'main/actor-detail.html', context=context)


class ActorDetailView(DetailView):
    template_name = 'main/actor-detail.html'
    model = models.Actor
    context_object_name = 'actor'
    slug_url_kwarg = 'actor_slug'


# def create_actor(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         form = forms.ActorForm(request.POST, request.FILES)
#         if form.is_valid():
#             models.Actor.objects.create(**form.cleaned_data)
#     else:
#         form = forms.ActorForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'main/create-actor.html', context=context)


class ActorCreateView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'form': forms.ActorForm(),
        }
        return render(request, 'main/create-actor.html', context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = forms.ActorForm(request.POST, request.FIELS)

        if form.is_valid():
            form.save()
            return redirect('main:actor-detail', actor_slug=form.cleaned_data['actor_slug'])

        context = {
            'form': form,
        }
        return render(request, 'main/create-actor.html', context=context)





