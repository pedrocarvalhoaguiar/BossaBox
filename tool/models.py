from django.db import models


class Tool(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    link = models.CharField(max_length=255, verbose_name='Link')
    descricao = models.CharField(max_length=255, verbose_name='Descrição')
    tags = models.CharField(max_length=255, verbose_name='Tags')