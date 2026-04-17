from django.shortcuts import render
from django.http import HttpResponseRedirect
from films.models import Film  
import random

def search_page(request):
    results = []
    query = ''
    random_film = None
    
    if request.method == 'GET' and 'random' in request.GET:
        films_count = Film.objects.count()
        if films_count > 0:
            random_index = random.randint(0, films_count - 1)
            random_film = Film.objects.all()[random_index]
    
    elif request.method == 'GET' and 'q' in request.GET:
        query = request.GET['q'].strip()
        
        if query:
            results = Film.objects.filter(
                title__iregex=query
            ) | Film.objects.filter(
                director__iregex=query
            ) | Film.objects.filter(
                actors__iregex=query
            ) | Film.objects.filter(
                genre__iregex=query
            )
    
    return render(request, 'websearch/search.html', {
        'results': results,
        'query': query,
        'random_film': random_film, 
        'total_films': Film.objects.count()  
    })