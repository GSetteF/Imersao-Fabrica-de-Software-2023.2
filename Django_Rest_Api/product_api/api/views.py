from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from .models import Product

# Create your views here.


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<int:id>',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-detail/<int:id>',
    }

    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request): #Criando nossa função responsável por mostrar todos os produtos
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True) 
    return Response(serializer.data)

@api_view(['GET'])
def ViewProduct(request, pk): #Mostrar apenas Um
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False) 
    return Response(serializer.data)

@api_view(['POST']) 
def CreateProduct(request): #Função responsavel por criar dados, obs: atentar ao formato JSON.
    serializer = ProductSerializer(data=request.data) 

    if serializer.is_valid(): #verificar se dado é valido
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def updateProduct(request, pk): #Função para atualizar
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteProduct(request, pk): #Função para deletar um dado.
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Item deletado.')