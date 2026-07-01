from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView

from rest_framework.viewsets import ModelViewSet

from . import models, forms


class CategoryViewSet(ListAPIView):
    queryset = models.Category.objects.all()



class CategoryListView(ListView):
    template_name = 'main/categories-list.html'
    model = models.Category
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    template_name = 'main/category-detail.html'
    model = models.Category
    context_object_name = 'category'


class MovieListView(ListView):
    template_name = 'main/movies-list.html'
    model = models.Movie
    context_object_name = 'movies'


class MovieDetailView(DetailView):
    template_name = 'main/movie-detail.html'
    model = models.Movie
    context_object_name = 'movie'
    slug_url_kwarg = 'movie_slug'


class MovieCreateView(CreateView):
    model = models.Movie
    form_class = forms.MovieForm

    def get_success_url(self):
        return reverse(
            'main:movie_detail',
            kwargs={'movie_slug': self.object.slug}
        )


class MovieUpdateView(UpdateView):
    model = models.Movie
    form_class = forms.MovieForm
    slug_url_kwarg = 'movie_slug'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse(
            'main:movie_detail',
            kwargs={'movie_slug': self.object.slug}
        )


class MovieDeleteView(DeleteView):
    model = models.Movie
    slug_url_kwarg = 'movie_slug'
    success_url = reverse_lazy('main:movies_list')


class ActorListView(ListView):
    template_name = 'main/actors-list.html'
    model = models.Actor
    context_object_name = 'actors'


class ActorDetailView(DetailView):
    template_name = 'main/actor-detail.html'
    model = models.Actor
    context_object_name = 'actor'
    slug_url_kwarg = 'actor_slug'


class ActorCreateView(CreateView):
    model = models.Actor
    form_class = forms.ActorForm

    def get_success_url(self):
        return reverse(
            'main:actor_detail',
            kwargs={'actor_slug': self.object.slug}
        )


class ActorUpdateView(UpdateView):
    model = models.Actor
    form_class = forms.ActorForm
    slug_url_kwarg = 'actor_slug'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse(
            'main:actor_detail',
            kwargs={'actor_slug': self.object.slug}
        )


class ActorDeleteView(DeleteView):
    model = models.Actor
    slug_url_kwarg = 'actor_slug'
    success_url = reverse_lazy('main:actors_list')


