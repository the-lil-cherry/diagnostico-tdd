from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.CharField(max_length=5000)
