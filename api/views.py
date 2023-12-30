from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ProductSerilizer
from .models import Product

@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'list' : '/product-list',
        'Detail view':'/product-details/<int:id>',
        'Create':'/product-create/',
        'Update':'/product-update/<int:id>',
        'Delete':'/product-delete/<int:id>'
    }
    return Response(api_urls)

@api_view(['GET'])
def ShowAll(request):
    Products = Product.objects.all()
    serializer = ProductSerilizer(Products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewproduct(request , pk):
    Products = Product.objects.get(id=pk)
    serializer = ProductSerilizer(Products,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createdata(request):
    serializer = ProductSerilizer(data= request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['POST'])
def update(request , pk):
    Products = Product.objects.get(id=pk)
    serializer = ProductSerilizer(instance=Product,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def delete(request , pk):
    Products = Product.objects.get(id=pk)
    Product.delete()
    return Response("Deleted")