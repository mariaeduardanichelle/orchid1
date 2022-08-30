from django.db import models

class Origen(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    pericias_treinadas = models.CharField(max_length=100)
    poder = models.CharField(max_length=1000000)

    def __str__(self):
      return self.nome

class Classe(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
      return self.nome


