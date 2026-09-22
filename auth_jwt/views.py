from django.shortcuts import render
from .serializers import SignUpSerializer3, LoginSerializer3, ProfileSerializer3, UpdateSerializer3, PasswordChangeSerializer3
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class SignUpView3(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer =SignUpSerializer3(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class LoginView3(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer3(data = request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        


class TokenRefresh(APIView):
        permission_classes = [AllowAny]
        def get(self, request):
            refresh = request.data.get('refresh')
            refresh_token  = RefreshToken(refresh)

            return Response(
                {'new_refreshtoken': str(refresh_token.access_token)}
            )


class Profile3(APIView):
    def get(self, request):
        user = request.user
        return Response(
            {
                'Account': ProfileSerializer3(user).data
            }
        )
    
class UpdateProfile3(APIView):
    def patch(self, request):
        serializer = UpdateSerializer3(instance = request.user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        



class PasswordChangeView3(APIView):
    def put(self,request):
        serializer = PasswordChangeSerializer3(instance = request.user, data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
