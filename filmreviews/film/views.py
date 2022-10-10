from django.shortcuts import render
from django.http import HttpResponse
from .models import Film

# Create your views here.

def home(request):
    zoek_term = request.GET.get('zoekFilm')
    if zoek_term:
        films = Film.objects.filter(title__icontains=zoek_term)
    else:
        films = Film.objects.all()
    return render(request, 'home.html',
        {
            'zoekTerm' : zoek_term,
            'films' :   films
        })

def over(request):
    return HttpResponse('<h1>Welkom op de over-ons pagina</h1>')
