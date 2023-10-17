import json
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from base.models import ProductSection, Products, Inventory, Dispatched
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
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
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
    serializer = ProductSerializer(product)
    return Response(serializer.data)

# Get Section
@api_view(['GET'])
def getSection(request, pk):
    section = get_object_or_404(ProductSection, pk=pk)
    serializer = SectionSerializer(section)
    return Response(serializer.data)


@api_view(['GET'])
def getInventoryDetails(request, pk):
    inventory =  get_object_or_404(Inventory, pk=pk)
    serializer = InventorySerializer(inventory)
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
        # Extract data from the serializer
        product_id = serializer.validated_data['product']
        quantity = serializer.validated_data['product_quantity']

        try:
            # Attempt to get an existing inventory entry for the product
            inventory_entry = Inventory.objects.get(product=product_id)
            # Update the existing entry by incrementing the quantity
            inventory_entry.product_quantity += quantity
            inventory_entry.save()
            return Response(InventorySerializer(inventory_entry).data)
        except Inventory.DoesNotExist:
            # If no existing entry, create a new one
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
 
    
# Update Stock by Outer Product Case Barcode
@api_view(['POST'])
def updateStockByOuterProductCaseBarcode(request):
    outer_product_case_barcode = request.data.get('outer_product_case_barcode')
    product_quantity = request.data.get('product_quantity', 1)  # Default to 1 if not provided
    product_last_action = request.data.get('product_last_action', 'Subtraction')
    product = get_object_or_404(Products, outer_product_case_barcode=outer_product_case_barcode)

    # Check if there's an existing inventory entry for the product
    try:
        inventory_entry = Inventory.objects.get(product=product)
        if product_last_action == 'Subtraction':
            # Subtract the provided quantity from the existing quantity
            if product_quantity <= inventory_entry.product_quantity:
                inventory_entry.product_quantity -= product_quantity
                inventory_entry.save()

                # Create a new Dispatched entry
                Dispatched.objects.create(
                    dispatch_quantity=product_quantity,
                    product=product,
                    inventory=inventory_entry
                )

            else:
                return Response(
                    {'Success': False, 'Message': 'Not Enough Stock For Subtraction...'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        elif product_last_action == 'Subtraction':
            inventory_entry.product_quantity += product_quantity
            inventory_entry.save()
        # Serialize and return the updated inventory entry
        serializer = InventorySerializer(inventory_entry)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Inventory.DoesNotExist:
        return Response(
            {'Success': False, 'Message': 'No Inventory Entry Found For The Provided Product...'},
            status=status.HTTP_404_NOT_FOUND
        )
        
        

# Get The Product ID via The Barcode

@api_view(['POST'])
def getProductInfoByBarcode(request):
    outer_product_case_barcode = request.data.get('outer_product_case_barcode')
    try:
        product = get_object_or_404(Products, outer_product_case_barcode=outer_product_case_barcode)
        product_id = product.product_id
        product_name = product.product_name
        return Response({'product_id': product_id, 'product_name': product_name})
    except Products.DoesNotExist:
        return Response(
            {'Success': False, 'Message': 'Product not found for the provided outer_product_case_barcode.'},
            status=status.HTTP_404_NOT_FOUND
        )
        
