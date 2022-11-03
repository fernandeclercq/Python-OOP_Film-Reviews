from django.urls import path, re_path
from . import views

urlpatterns = [
    path('registreer/', views.registreer, name='registreer'),
]