from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from .models import Film
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    zoekTerm = request.GET.get('zoekFilm')
    if zoekTerm:
        films = Film.objects.filter(title__icontains=zoekTerm)
    else:
        films = Film.objects.all() #Fetch all Film objects from database
    return render(request, 'home.html', {'zoekTerm': zoekTerm, 'films': films})

def over(request):
    return HttpResponse('<h1>Welkom op de over-ons pagina</h1>')


def detail(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    return render(request, 'detail.html', {'film': film})