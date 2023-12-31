from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import products
from .models import Product
from .serializers import ProductSerializer

# Create your views here.


def getRoutes(request):
    return JsonResponse('Hello', safe=False)


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def getProduct(request, pk):
#     selectedProduct = None
#     for product in products:
#         if product['_id'] == pk:
#             selectedProduct = product

#     if selectedProduct:
#         return Response(selectedProduct)
#     else:
#         return Response("Unable to find product")

@api_view(['GET'])
def getProduct(request, pk):
    selectedProduct = Product.objects.get(_id=pk)
    serializer = ProductSerializer(selectedProduct, many=False)
    return Response(serializer.data)
