from django.urls import path
from . import views

urlpatterns = [
    path('over/', views.over, name='over'),
    path('<int:film_id>', views.detail, name='detail')
]
