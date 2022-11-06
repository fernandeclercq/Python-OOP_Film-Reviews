from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from .models import Film, Review
from django.shortcuts import get_object_or_404, redirect
from .forms import ReviewForm

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


def maakreview(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    if request.method == 'GET':
        return render(request, 'maakreview.html', {'form':ReviewForm(), 'film': film})
    else:
        try:
            form = ReviewForm(request.POST)
            nieuwReview = form.save(commit=False)
            nieuwReview.user = request.user
            nieuwReview.film = film
            nieuwReview.save()
            return redirect('detail', nieuwReview.film.id)
        except ValueError:
            return render(request, 'maakreview.html', {'form':ReviewForm(), 'error': 'Niet correcte data'})
