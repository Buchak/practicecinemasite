from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class CategoryMovieInline(admin.TabularInline):
    model = models.Category.movies.through
    extra = 1


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    list_display_links = ('pk', 'title',)
    ordering = ('-pk',)
    search_fields = ('pk', 'title')
    inlines = [CategoryMovieInline]


class ActorInline(admin.TabularInline):
    model = models.Movie.actors.through
    extra = 1


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description_short', 'release_date')
    list_display_links = ('pk', 'title', 'release_date')
    ordering = ('-pk',)
    search_fields = ('pk', 'title', 'release_date')
    inlines = [ActorInline]
    filter_horizontal = ('category',)
    readonly_fields = ('poster_preview',)
    fieldsets = (
        (None, {
            'fields': ('poster_preview', 'poster', 'title', 'category'),
        }),
        ('Release Date', {
            'fields': ('release_date',)
        }),
        ('Movie Description', {
            'fields': ('description',),
            'classes': ('collapse',),
        }),
        ('Slug', {
            'fields': ('slug',),
            'classes': ('collapse',)
        })
    )

    def description_short(self, obj: models.Movie):
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + '...'

    @admin.display(description='Poster Image')
    def poster_preview(self, obj: models.Movie):
        if obj.poster:
            return mark_safe(
                f'<img src="{obj.poster.url}" width="200" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />')
        return "Not image"


class ActorMovieInline(admin.TabularInline):
    model = models.Actor.movies.through
    extra = 0
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'full_name', 'description_short', 'birth_date')
    list_display_links = ('pk', 'full_name', 'birth_date')
    ordering = ('-pk',)
    search_fields = ('pk', 'full_name', 'birth_date')
    readonly_fields = ('photo_preview',)
    inlines = [ActorMovieInline]
    fieldsets = (
        (None, {
            'fields': ('photo_preview', 'photo', 'last_name', 'first_name', 'middle_name', 'birth_date'),
        }),
        ('Description', {
            'fields': ('description',),
            'classes': ('collapse',),
        }),
        ('Slug', {
            'fields': ('slug',),
            'classes': ('collapse',),
        }),
    )

    def description_short(self, obj: models.Movie):
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + '...'

    def full_name(self, obj: models.Actor):
        middle_name = '' if obj.middle_name == '' else obj.middle_name
        return f'{obj.last_name} {obj.first_name} {middle_name}'

    @admin.display(description='Photo Image')
    def photo_preview(self, obj: models.Actor):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" width="200" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />')
        return "Not image"

