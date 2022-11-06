from operator import mod
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Film(models.Model):
    title = models.CharField(max_length=100)
    beschrijving = models.CharField(max_length=250)
    afbeelding = models.ImageField(upload_to='film/afbeeldingen/')
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title

class Review(models.Model):
    tekst = models.CharField(max_length=100)
    datum = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    opnieuwBekijken = models.BooleanField()

    def __str__(self) -> str:
        return self.tekst
