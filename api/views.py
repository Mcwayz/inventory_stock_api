import json
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from base.models import ProductSection, Products, Inventory
from .serializers import ProductSerializer, SectionSerializer, InventorySerializer

#                            #
#                            #
#                            #
#    GET Request Methods     #
#                            #
#                            #
#                            #


# Get Product Sections
@api_view(['GET'])
def getSections(request):
    sections = ProductSection.objects.all()
    serializer = SectionSerializer(sections, many=True)
    return Response(serializer.data)


# Get Products
@api_view(['GET'])
def getProducts(request):
    sections = Products.objects.all()
    serializer = ProductSection(sections, many=True)
    return Response(serializer.data)


# Get Products
@api_view(['GET'])
def getInventory(request):
    inventory = Inventory.objects.all()
    serializer = InventorySerializer(inventory, many=True)
    return Response(serializer.data)


# Get Product
@api_view(['GET'])
def getProduct(request, pk):
    product = get_object_or_404(Products, pk=pk)
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

# Get Section

@api_view(['GET'])
def getSection(request, pk):
    section = get_object_or_404(ProductSection, pk=pk)
    serializer = SectionSerializer(section, many=True)
    return Response(serializer.data)


#                            #
#                            #
#                            #
# End Of GET Request Methods #
#                            #
#                            #
#                            # 






#                            #
#                            #
#                            #
#   POST Request Methods     #
#                            #
#                            #
#                            #


# Add Product Section
@api_view(['POST'])
def addSection(request):
    serializer = SectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

# Add Product
@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
# Add Inventory
@api_view(['POST'])
def addStock(request):
    serializer = InventorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)