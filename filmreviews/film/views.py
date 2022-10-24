from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Welkom op de homepagina</h1>')

def over(request):
    return HttpResponse('<h1>Welkom op de over-ons pagina</h1>')