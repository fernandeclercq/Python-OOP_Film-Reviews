from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    zoekTerm = request.GET.get('zoekFilm')
    return render(request, 'home.html', {'naam':'Fernando', 'zoekTerm': zoekTerm})

def over(request):
    return HttpResponse('<h1>Welkom op de over-ons pagina</h1>')