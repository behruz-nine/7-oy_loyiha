

from django.shortcuts import render
from .serializers import AccountSerializer, LoginSerializer, AccountUpdateSerializer, PasswordChangeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Account
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly



# Create your views here.

class SignUpView(APIView):
    permission_classes = [AllowAny]
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
    permission_classes = [AllowAny]
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
    

class ProfileUpdateView(APIView):
    def patch(self, request):
        serializer = AccountUpdateSerializer(instance = request.user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            
            return Response(
                {
                    'msg': 'Account is updated successfully',
                    'account': serializer.data,
                    'status': status.HTTP_201_CREATED
                }
            )


class PasswordChangeView(APIView):
    def put(self, request):
        serializer = PasswordChangeSerializer(instance = request.user, data= request.data)
        if serializer.is_valid():
            user = request.user
            old_pass = serializer.validated_data['old_password']
            new_pass = serializer.validated_data['new_password']
            current_user = authenticate(username = user.username, password = old_pass)

            if current_user is None:
                raise ValidationError('Eski parol xato kiritildi')
            
            current_user.set_password(raw_password = new_pass)
            current_user.save()

            return Response(
                {
                    'msg': 'Password is changed successfully',
                    'password': new_pass,
                    'status': status.HTTP_200_OK
                }
            )



