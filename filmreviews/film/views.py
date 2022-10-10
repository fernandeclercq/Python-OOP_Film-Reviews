from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    zoek_term = request.GET.get('zoekfilm')
    return render(request, 'home.html', {'name':'Fernando Declercq', 'zoekTerm': zoek_term})

def over(request):
    return HttpResponse('<h1>Welkom op de over-ons pagina</h1>')
