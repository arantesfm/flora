from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    
    familia = models.CharField(max_length=300)
    genero = models.CharField(max_length=300)
    especie = models.CharField(max_length=300)
    autor = models.CharField(max_length=300)
    texto = models.TextField()
    habito = models.CharField(max_length=300)
    vernacular = models.CharField(max_length=300)
    floracao = models.CharField(max_length=300)
    frutificacao = models.CharField(max_length=300)
    origem = models.CharField(max_length=300)
    mapa = models.TextField()
    referencias = models.TextField()


    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title