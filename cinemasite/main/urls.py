from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('category/', views.categories_list, name='categories_list'),
    path('category/<slug:category_slug>/', views.category_detail, name='category_detail'),
]