from django.db import models
from django.utils.text import slugify

from unidecode import unidecode


class Actor(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField()
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    photo = models.ImageField(upload_to='actors_photo/', blank=True, null=True)

    def __str__(self):
        middle_name = '' if self.middle_name == '' else self.middle_name
        return f'{self.last_name} {self.first_name} {middle_name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.last_name + self.first_name))
        super().save(*args, **kwargs)


class Movie(models.Model):
    actor = models.ForeignKey(Actor, related_name='movie', on_delete=models.CASCADE, blank=True)

    title = models.CharField(max_lenhth=200)
    description = models.TextField(blank=True)
    release_date = models.DateField()
    slug = models.SlugField(unique=True, blank=True)
    poster = models.ImageField(upload_to='movie_photo/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)


