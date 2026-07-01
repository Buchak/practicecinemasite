from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from . import models, forms, serializers


class CategoryListAPIView(ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filetr_backends = [
        SearchFilter,
        OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ['title',]
    ordering_fields = ['pk', 'title']
    ordering = ['-pk']
    filterset_fields = ['title',]


class CategoryListView(ListView):
    template_name = 'main/categories-list.html'
    model = models.Category
    context_object_name = 'categories'


class CategoryDetailAPIView(RetrieveAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryDetailSerializer
    lookup_field = 'slug'


class CategoryDetailView(DetailView):
    template_name = 'main/category-detail.html'
    model = models.Category
    context_object_name = 'category'


class MovieViewSet(ModelViewSet):
    queryset = models.Movie.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        OrderingFilter,
        DjangoFilterBackend,
    ]
    ordering = ['-pk',]
    filterset_fields = [
        'title',
        'category',
        'release_date',
    ]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MovieSerializer
        if self.action == 'retrieve':
            return serializers.MovieDetailSerializer

        return serializers.MovieDetailSerializer


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


class ActorViewSet(ModelViewSet):
    queryset = models.Actor.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        SearchFilter,
        OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'first_name',
        'last_name',
        'middle_name',
    ]
    ordering = ['-pk',]
    filterset_fields = [
        'last_name',
        'first_name',
        'middle_name',
        'birth_date',
    ]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ActorSerializer
        if self.action == 'retrieve':
            return serializers.ActorDetailSerializer

        return serializers.ActorDetailSerializer


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


