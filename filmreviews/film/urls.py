from django.urls import path, re_path
from . import views

urlpatterns = [
    path('<int:film_id>', views.detail, name='detail')
]
