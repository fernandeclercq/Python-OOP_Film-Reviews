from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # Het Django user model
from django.contrib.auth import login # De login functie
from django.shortcuts import redirect # De redirect functie
from django.db import IntegrityError

# Create your views here.

def registreer(request):

    try:

        if request.method == 'GET':
            return render(request, 'registreer.html', {'form': UserCreationForm})
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
                return render(request, 'registreer.html', {'form': UserCreationForm, 'error': "Wachtwoorden matchen niet" })

    except IntegrityError:
        return render(request, 'registreer.html', {'form':UserCreationForm, 'error': 'Gebruikersnaam is reeds gebruikt'})
