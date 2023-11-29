from django.db import models
from django.utils import timezone


#Armazena as informações das dividas

class Financas(models.Model):    
    banco = models.CharField(max_length=10000)
    valor_Divida = models.FloatField(default=0)
    renegociado = models.BooleanField(default=False)
    qt_parcelas = models.IntegerField(default=0)
    valor_total_parcelado = models.FloatField(default=0)
    data_renegociacao = models.DateField(default=timezone.now)    
    data_pagamento = models.DateField(blank=True, null=True)
    parcelas_pagas = models.IntegerField(default=0)

#Armazenas as informações das compras
class Compras(models.Model):
    produto = models.CharField(max_length=100)
    valor = models.FloatField(default=0)
    parcelado = models.BooleanField(default=False)
    qt_parcelas = models.IntegerField(default=0)
    juros = models.BooleanField(default=False)
