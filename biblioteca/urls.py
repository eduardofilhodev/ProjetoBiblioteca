from django.urls import path
from . import views

urlpatterns = [

    path("autores/", views.autores, name="autores"),

    path("livros/", views.livros, name="livros"),

]