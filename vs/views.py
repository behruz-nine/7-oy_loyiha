from django.shortcuts import render
from drf.models import Product
from rest_framework.response import Response
from rest_framework import status
from drf.serializers import ProductSerializer
from rest_framework.viewsets import ViewSet
# Create your views here.


class CreateProductViewSet(ViewSet):
    queryset = Product.objects.all()
    def create(self, request):
        serializer = ProductSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'msg': 'Product is created successfully',
                    'status': status.HTTP_201_CREATED
                }
            )


class ListProductViewSet(ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(
            {
                'products': serializer.data,
                'status': status.HTTP_200_OK
            }
        )
    

class DetailProductViewSet(ViewSet):
    queryset = Product.objects.all()
    def retrieve(self,request, pk):
        product = Product.objects.filter(id = pk).first()
        serializer = ProductSerializer(product)
        return Response(
            {
                'product': serializer.data,
                'status': status.HTTP_200_OK
            }
        )
    

class PutProductViewSet(ViewSet):
    queryset =Product.objects.all()
    def update(self, request, pk):
        product = Product.objects.filter(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(
            {
                'msg': 'Product is updated successfully',
                'status': status.HTTP_200_OK
            }
        )


class PatchProductViewSet(ViewSet):
    queryset = Product.objects.all()
    def partial_update(self, request, pk):
        product = Product.objects.filter(id=pk).first()
        serialiser = ProductSerializer(instance=product, data=request.data, partial=True)
        if serialiser.is_valid():
            serialiser.save()
        return Response(
            {
                'msg': 'Product is updated partially',
                'status': status.HTTP_200_OK
            }
        )
    

class DestroyProductViewSet(ViewSet):
    queryset = Product.objects.all()
    def destroy(self, request, pk):
        product = Product.objects.filter(id=pk).first()
        product.delete()
        return Response(
            {
                'msg': 'Product is deleted successfully',
                'status': status.HTTP_200_OK
            }
        )

        