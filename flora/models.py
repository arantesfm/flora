from django.db import models
from django.utils import timezone
import os
from django.conf import settings


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


    def endereco_imagem(self, foto=1):
        return 'imagens/{0}-{1}/{0}-{1}-{2}.jpg'.format(self.genero, self.especie, foto)

    def endereco_icone(self, icone=1):
        return 'imagens/{0}-{1}/ico-{0}-{1}-{2}.jpg'.format(self.genero, self.especie, icone)


    def todas_imagens(self):
        pasta_do_genero = 'imagens/{}-{}'.format(self.genero, self.especie)
        caminho_completo_da_pasta = '{}/{}'.format(settings.STATIC_ROOT,pasta_do_genero)
        imagens_encontradas = []
        for img in os.listdir  (caminho_completo_da_pasta):
            if not img.startswith('ico'):
               img_dict = {}
               img_dict['img'] = '{}/{}'.format(pasta_do_genero, img)
               img_dict['ico'] = '{}/ico-{}'.format(pasta_do_genero, img)
               imagens_encontradas.append(img_dict)
        return imagens_encontradas