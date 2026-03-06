import datetime

from django.db import models
from django.forms import ValidationError

class Autor(models.Model):

    nome = models.CharField(max_length=100, unique=True)

    email = models.EmailField()

    def __str__(self):
        return self.nome


class Livro(models.Model):

    titulo = models.CharField(max_length=200)

    ano = models.IntegerField()

    isbn = models.CharField(max_length=13, unique=True)

    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name="livros"
    )

    def clean(self):
        ano_atual = datetime.date.today().year

        if self.ano > ano_atual:
            raise ValidationError("O ano não pode ser maior que o ano atual.")

    def __str__(self):
        return self.titulo
