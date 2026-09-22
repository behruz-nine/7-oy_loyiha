from auth_.models import Account
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token

class SignUpSerializer2(serializers.ModelSerializer):
    id = serializers.CharField(read_only = True)
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user  = Account.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        user= super().to_representation(instance)
        return {
            'msg': 'Account muvaffaqiiyatli yaratildi',
            'data': user
        }
    

class LoginSerializer2(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def create(self, validated_data):
        password = validated_data.get('password')
        username = validated_data.get('username')
        
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError('Username yoki parol xato')
        
        token, created = Token.objects.get_or_create(user = user)

        u = token.key
        
        validated_data['u'] = u

        return validated_data
    

    
    def to_representation(self, validated_data):
        token  = validated_data['u']
        return {
            'msg': 'Tizimga muvaffaqiyatli kirildi',
            'token': token
        }
        

class PasswordChangeSerializer2(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    conf_password = serializers.CharField()

    def validate(self, data):
        old_password = data.get('old_password')
        request = self.context['request']
        user = request.user

        current_user = authenticate(username = user.username, password = old_password)
        if current_user is None:
            raise ValidationError('Eski parol xato')
        
        return data

    
    def save(self, **kwargs):
        request = self.context['request']
        user = request.user
        new_password = self.validated_data['new_password']
        user.set_password(new_password)
        user.save()
        return user
    

    def to_representation(self, instance):
        return {'message': "Parol o\'zgartirildi"}


        
        







        