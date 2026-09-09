from django.shortcuts import render
from .serializers import AccountSerializer, LoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token



# Create your views here.

class SignUpView(APIView):
    def post(self, request):
        serializer = AccountSerializer(data = request.data)
        if serializer.is_valid():
            user = Account.objects.create_user(**serializer.validated_data)
            user.save()
        
            

            return Response(
                {
                    'msg': 'Account is created successfully',
                    'Account': AccountSerializer(user).data,
                    'status': status.HTTP_201_CREATED
                }
            )
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data= request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            
            if not user:
                raise ValidationError('Username yoki parol xato')
            else:
                token, create = Token.objects.get_or_create(user = user)

                return Response(
                    {
                        'msg': 'Entery is successfully',
                        'token': token.key,
                        'status': status.HTTP_200_OK
                    }
                )
            
class ProfileView(APIView):
    def get(self, request):
        
        user = request.user

        return Response(
            {
                'profile': AccountSerializer(user).data,
                'status': status.HTTP_200_OK
            }
        )
