from rest_framework import serializers
from .models import Financas, Compras

class FinancasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financas
        fields = ('banco', 'valor_Divida', 'renegociado', 'qt_parcelas', 'valor_total_parcelado', 'data_renegociacao', 'data_pagamento', 'parcelas_pagas')

class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = ('produto', 'valor', 'parcelado', 'qt_parcelas', 'juros')