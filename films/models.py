from django.db import models

from django.db import models

class Film(models.Model):
    
    title = models.CharField(
        max_length=200, 
        verbose_name="Название фильма",
        help_text="Полное название фильма"
    )
    
    year = models.IntegerField(
        verbose_name="Год выпуска",
        help_text="Год выхода фильма"
    )
    
    director = models.CharField(
        max_length=100, 
        verbose_name="Режиссер",
        help_text="ФИО режиссера"
    )
    
    actors = models.TextField(
        verbose_name="Актеры",
        help_text="Список актеров через запятую"
    )
    
    genre = models.CharField(
        max_length=100, 
        verbose_name="Жанр",
        help_text="Основной жанр фильма"
    )
    
    description = models.TextField(
        verbose_name="Описание",
        blank=True,  
        help_text="Краткое описание сюжета"
    )
    
    
    created_at = models.DateTimeField(
        auto_now_add=True,  
        verbose_name="Дата добавления"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,  
        verbose_name="Дата обновления"
    )
    
   
    def __str__(self):
        return f"{self.title} ({self.year})"
    
    
    class Meta:
        verbose_name = "Фильм" 
        verbose_name_plural = "Фильмы"  
        ordering = ['-created_at']  