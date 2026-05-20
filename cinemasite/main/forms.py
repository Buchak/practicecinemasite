from django import forms

from . import models


class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = ('title', 'poster', 'release_date', 'description')

class ActorForm(forms.ModelForm):
    class Meta:
        model = models.Actor
        fields = ('last_name', 'first_name', 'middle_name', 'photo', 'birth_date', 'description')
