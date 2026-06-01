from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='categories_list'),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('movies/', views.movies_list, name='movies_list'),
    path('movies/<slug:movie_slug>/', views.movie_detail, name='movie_detail'),
    path('actors/', views.actors_list, name='actors_list'),
    path('actors/<slug:actor_slug>/', views.actor_detail, name='actor_detail'),
    path('create-movie/', views.create_movie, name='create_movie'),
    path('create-actor/', views.create_actor, name='create_actor'),
]