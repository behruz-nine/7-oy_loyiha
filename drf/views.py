from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product


# Create your views here.


@api_view(['POST'])
def create_product(request):
    product_name = request.data.get('product_name')
    description = request.data.get('description')
    price  = request.data.get('price')
    quantity = request.data.get('quantity')

    product = Product.objects.create(
        product_name=product_name,
        description=description,
        price=price,
        quantity=quantity
    )
    product.save()

    return Response(
        {
            'msg': 'Product created successfully',
            'status':  status.HTTP_201_CREATED
         }  
    )

#====================================================

@api_view(['GET'])
def getproducts(request):
    products = Product.objects.all()
    project_list = []
    for product in products:
        project_list.append(
            {'product_name': product.product_name,
             'description': product.description,
             'price': product.price,
             'quantity': product.quantity,
             'product id': product.id}
            )
    return Response(
        {
            'msg': project_list,
            'status': status.HTTP_201_CREATED
        }
    )

#====================================================

@api_view(['GET'])
def product_details(request, product_id):
    product = Product.objects.get(id = product_id)
    product_detail = {'id': product.id, 
                      'product_name': product.product_name,
                      'description': product.description,
                      'price': product.price,
                      'quantity': product.quantity}
    
    return Response(
        { 'msg': 'Product topildi'}, status= status.HTTP_201_CREATED
    )



