from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import SignUpSerializer2, LoginSerializer2, PasswordChangeSerializer2
from rest_framework.permissions import AllowAny

# Create your views here.

class SignUpView2(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = SignUpSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        



class LoginView2(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer2(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        


class ProfileView2(APIView):
    def get(self, request):
        user = request.user
        return Response(
            {
                'profile': SignUpSerializer2(user).data,
                'status': status.HTTP_200_OK
            }
        )
    


class ProfileUpdateView2(APIView):
    def patch(self, request):
        serializer = SignUpSerializer2(instance= request.user, data= request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'msg': 'Account muvaffaqiyatli o\'zgartirildi',
                    'Account': serializer.data,
                    'status': status.HTTP_200_OK
                }
            )
        

class PasswordChangeView2(APIView):
    def put(self,request):
        serializer = PasswordChangeSerializer2(instance = request.user, data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
