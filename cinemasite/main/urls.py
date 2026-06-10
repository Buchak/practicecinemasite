from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='categories_list'),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),

    path('movies/', views.MovieListView.as_view(), name='movies_list'),
    path('create-movie/', views.MovieCreateView.as_view(), name='create_movie'),
    path('movies/<slug:movie_slug>/update/', views.MovieUpdateView.as_view(), name='movie_update'),
    path('movies/<slug:movie_slug>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),
    path('movies/<slug:movie_slug>/', views.MovieDetailView.as_view(), name='movie_detail'),

    path('actors/', views.ActorListView.as_view(), name='actors_list'),
    path('create-actor/', views.ActorCreateView.as_view(), name='create_actor'),
    path('actors/<slug:actor_slug>/', views.ActorDetailView.as_view(), name='actor_detail'),
]