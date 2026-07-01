from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

routers_movies = DefaultRouter()
routers_movies.register('movies', views.MovieViewSet)
routers_actors = DefaultRouter()
routers_actors.register('actors', views.ActorViewSet)

app_name = 'main'

urlpatterns = [
    path('api/category/', views.CategoryListAPIView.as_view(), name='category_list_api'),
    path('api/category/<slug:slug>', views.CategoryDetailAPIView.as_view(), name='category_detail_api'),
    path('api/movie/', include(routers_movies.urls)),
    path('api/actor/', include(routers_actors.urls)),


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
    path('actors/<slug:actor_slug>/update', views.ActorUpdateView.as_view(), name='actor_update'),
    path('actors/<slug:actor_slug>/delete', views.ActorDeleteView.as_view(), name='actor_delete'),
]