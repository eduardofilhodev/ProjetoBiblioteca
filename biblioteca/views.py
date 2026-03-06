from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Autor, Livro


def autores(request):

    erro = None

    if request.method == "POST":

        if "criar" in request.POST:

            nome = request.POST["nome"]
            email = request.POST["email"]

            if Autor.objects.filter(nome__iexact=nome).exists():
                erro = "Já existe um autor com esse nome."
            else:
                Autor.objects.create(
                    nome=nome,
                    email=email
                )
                return redirect("autores")


        elif "editar" in request.POST:

            autor = Autor.objects.get(id=request.POST["id"])
            nome = request.POST["nome"]
            email = request.POST["email"]

            if Autor.objects.filter(nome__iexact=nome).exclude(id=autor.id).exists():
                erro = "Já existe outro autor com esse nome."
            else:
                autor.nome = nome
                autor.email = email
                autor.save()
                return redirect("autores")


        elif "deletar" in request.POST:

            autor = Autor.objects.get(id=request.POST["id"])
            autor.delete()
            return redirect("autores")

    autores = Autor.objects.all()

    return render(request, "autores.html", {
        "autores": autores,
        "erro": erro
    })

def livros(request):

    erro = None

    if request.method == "POST":

        if "criar" in request.POST:
            try:
                Livro.objects.create(
                    titulo=request.POST["titulo"],
                    ano=request.POST["ano"],
                    isbn=request.POST["isbn"],
                    autor_id=request.POST["autor"]
                )
                return redirect("livros")

            except IntegrityError:
                erro = "Já existe um livro com esse ISBN."

        elif "editar" in request.POST:

            livro = Livro.objects.get(id=request.POST["id"])

            try:
                livro.titulo = request.POST["titulo"]
                livro.ano = request.POST["ano"]
                livro.isbn = request.POST["isbn"]
                livro.autor_id = request.POST["autor"]

                livro.save()
                return redirect("livros")

            except IntegrityError:
                erro = "Já existe um livro com esse ISBN."

        elif "deletar" in request.POST:

            livro = Livro.objects.get(id=request.POST["id"])
            livro.delete()
            return redirect("livros")

    livros = Livro.objects.all()
    autores = Autor.objects.all()

    return render(request, "livros.html", {
        "livros": livros,
        "autores": autores,
        "erro": erro
    })