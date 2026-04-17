from django.contrib import admin
from django.urls import path, include  # ← добавить include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('websearch.urls')),  # ← веб-поиск на главной
]