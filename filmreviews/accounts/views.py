from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import GebruikerRegistratieForm
from django.contrib.auth.models import User # Het Django user model
from django.contrib.auth import login # De login functie
from django.shortcuts import redirect # De redirect functie
from django.db import IntegrityError
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def registreer(request):

    try:

        if request.method == 'GET':
            return render(request, 'registreer.html', {'form': GebruikerRegistratieForm})
        else:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(
                    request.POST['username'],
                    password = request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'registreer.html', {'form': GebruikerRegistratieForm, 'error': "Wachtwoorden matchen niet" })

    except IntegrityError:
        return render(request, 'registreer.html', {'form':GebruikerRegistratieForm, 'error': 'Gebruikersnaam is reeds gebruikt'})

def loguit(request):
    logout(request)
    return redirect('home')


def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form':AuthenticationForm})
    else:
        user = authenticate(request,
        username = request.POST['username'],
        password = request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'form':AuthenticationForm(), 'error':'Gebruikersnaam bestaat niet'})
        else:
            login(request, user)
            return redirect('home')