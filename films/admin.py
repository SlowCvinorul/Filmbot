from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from .models import Film

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'director', 'genre']
    search_fields = ['title', 'director', 'actors']
    list_filter = ['year', 'genre']
    list_per_page = 20
    
    