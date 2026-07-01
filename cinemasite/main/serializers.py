from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['title', 'slug']


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['title', 'slug', 'movies']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ['title', 'poster', 'category', 'release_date']


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ['title', 'poster', 'category', 'release_date', 'actors', 'description']


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Actor
        fields = ['last_name', 'first_name', 'middle_name', 'photo', 'birth_date']


class ActorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Actor
        fields = ['last_name', 'first_name', 'middle_name', 'photo', 'birth_date', 'description']