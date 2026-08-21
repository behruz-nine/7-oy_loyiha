from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Product

# Create your views here.

class CreateProduct(APIView):
    def post(self, request):
        serializer = ProductSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'msg': 'Product is created successfully',
                    'status': status.HTTP_201_CREATED
                }
            )
        
class ListProduct(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(
            {
                'Products': serializer.data,
                'status': status.HTTP_200_OK
            }
        )
    

class DetailProduct(APIView):
    def get(self, request, product_id):
        product = Product.objects.filter(id=product_id).first()
        serializer = ProductSerializer(product)

        return Response(
            {
                'Product': serializer.data,
                'status': status.HTTP_200_OK
            }
        )
    
class PutProduct(APIView):
    def put(self, request, product_id):
        product = Product.objects.filter(id=product_id).first()
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'msg': 'Product is updated successfully',
                    'status': status.HTTP_200_OK
                }
            )


class PatchProduct(APIView):
    def patch(self, request, product_id):
        product = Product.objects.filter(id=product_id).first()
        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'msg': 'Product is updated partially',
                    'status': status.HTTP_200_OK
                }
            )
        
class DeleteProduct(APIView):
    def delete(self, request, product_id):
        product = Product.objects.filter(id=product_id).first()
        product.delete()
        return Response(
            {
                'msg': 'Product is deleted successfully',
                'status': status.HTTP_204_NO_CONTENT
            }
        )

