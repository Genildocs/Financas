from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Financas, Compras
from .serializers import FinancasSerializer, ComprasSerializer
# Create your views here.

@csrf_exempt
def financasApi(request):
    if request.method == 'GET':
        financas = Financas.objects.all()
        financas_serializer = FinancasSerializer(financas, many=True)
        #o parametro safe igual a false foi usado para informar ao django que enquanto estamos tentando converter,
        # os dados para json é na verdade um formato valido e estamos bem se houver erros.
        return JsonResponse(financas_serializer.data, safe=False)
    elif request.method == 'POST':
        financas_data = JSONParser().parse(request)
        financas_serializer = FinancasSerializer(data=financas_data)
        if financas_serializer.is_valid():
            #se o modelo for valido salvamos no banco de dados.
            financas_serializer.save()
            return JsonResponse("Adicionado com sucesso", safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    elif request.method == 'PUT':
        financas_data = JSONParser().parse(request)
        #Estamos capturando o registro existente usando o id de financas
        financas = Financas.objects.get(financa_id = financas_data['financa_id'])
        #estamos mapeando os dados com novos valores utilizando a classe serialize
        financas_serializer = FinancasSerializer(financas, data=financas_data)
        if financas_serializer.is_valid():
            financas_serializer.save()
            return JsonResponse("Atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar", safe=False)
    elif request.method == 'DELETE':
        financas = Financas.objects.get(financa_id=id)
        financas.delete()
        return JsonResponse("Deletado com sucesso", safe=False)
    return JsonResponse("Erro ao deletar", safe=False)

@csrf_exempt
def ComprasApi(request):
    if request.method == 'GET':
        compras = Compras.objects.all()
        compras_serializer = ComprasSerializer(compras, many=True)
        #o parametro safe igual a false foi usado para informar ao django que enquanto estamos tentando converter,
        # os dados para json é na verdade um formato valido e estamos bem se houver erros.
        return JsonResponse(compras_serializer.data, safe=False)
    elif request.method == 'POST':
        compras_data = JSONParser().parse(request)
        compras_serializer = ComprasSerializer(data=compras_data)
        if compras_serializer.is_valid():
            #se o modelo for valido salvamos no banco de dados.
            compras_serializer.save()
            return JsonResponse("Adicionado com sucesso", safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    elif request.method == 'PUT':
        compras_data = JSONParser().parse(request)
        #Estamos capturando o registro existente usando o id de compras
        compras = Compras.objects.get(compras_id = compras_data['compras_id'])
        #estamos mapeando os dados com novos valores utilizando a classe serialize
        compras_serializer = ComprasSerializer(compras, data=compras_data)
        if compras_serializer.is_valid():
            compras_serializer.save()
            return JsonResponse("Atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar", safe=False)
    elif request.method == 'DELETE':
        compras = Compras.objects.get(compras_id=id)
        compras.delete()
        return JsonResponse("Deletado com sucesso", safe=False)
    return JsonResponse("Erro ao deletar", safe=False)