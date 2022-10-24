from django.shortcuts import render


# Create your views here.


def nieuws(request):
    return render(request, 'nieuws.html')