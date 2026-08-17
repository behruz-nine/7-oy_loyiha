from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Product


# Create your views here.


@api_view(['POST', 'GET'])
def create_get_product(request):
    if request.method == 'POST':
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

    if request.method == 'GET':
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

@api_view(['GET','PUT','PATCH', 'DELETE'])
def product_dppd(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id = product_id)
        product_detail = {'id': product.id, 
                        'product_name': product.product_name,
                        'description': product.description,
                        'price': product.price,
                        'quantity': product.quantity}
        
        return Response(
            { 'msg': product_detail}, status= status.HTTP_201_CREATED
        )

    if request.method == 'PUT':
        product = Product.objects.filter(id = product_id).first()
        if product:
            product.product_name = request.data.get('product_name')
            product.description = request.data.get('description')
            product.price = request.data.get('price')
            product.quantity = request.data.get('quantity')

            product.save()

        return Response(
            {
                'msg': 'Product updated successfully',
                'status': status.HTTP_200_OK
            }
        )


    if request.method == 'PATCH':
        product = Product.objects.filter(id=product_id).first()
        if not product:
            raise NotFound('This product is not founded')
        
        product_name = request.data.get('product_name')
        description = request.data.get('description')
        price = request.data.get('price')
        quantity = request.data.get('quantity')

        if product_name:
            product.product_name = product_name

        if description:
            product.description = description

        if price:
            product.price = price

        if quantity:
            product.quantity = quantity

        product.save()

        return Response(
            {
                'msg': 'Product is updated partially',
                'status': status.HTTP_200_OK
            }
        )


    if request.method == 'DELETE':
        product = Product.objects.filter(id = product_id).first()
        product.delete()

        return Response(
            {
                'msg': 'Product is deleted successfully',
                'status': status.HTTP_200_OK
            }
        )

#==============================================================

    
