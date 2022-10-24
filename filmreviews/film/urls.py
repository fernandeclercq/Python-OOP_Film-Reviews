from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('over/', views.over, name='over')
]
