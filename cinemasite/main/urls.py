from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('category/', views.categories_list, name='categories_list'),
    path('category/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('movies/', views.movies_list, name='movies_list'),
    path('movies/<slug:movie_slug>/', views.movie_detail, name='movie_detail'),
    path('actors/<slug:actor_slug>/', views.actor_detail, name='actor_detail'),
]