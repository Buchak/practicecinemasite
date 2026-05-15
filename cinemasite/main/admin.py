from django.contrib import admin

from . import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_short', 'release_date')
    link_display = ('title', 'release_date')



    def description_short(self, obj: models.Movie):
        if len(obj.description) < 48:
            return obj.description
        return obj.description[48:] + '...'


@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    pass

