from rest_framework import serializers
from auth_.models import Account
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpSerializer3(serializers.ModelSerializer):
    id = serializers.CharField(read_only = True)
    conf_password = serializers.CharField(write_only=True)
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'conf_password', 'first_name', 'last_name']
    
    def validate(self, attrs):
        password = attrs.get('password')
        conf_password = attrs.get('conf_password')
        username = attrs.get('username')

        if password != conf_password and password and conf_password:
            raise ValidationError('Parollar mos emas')
        return attrs
    

    def create(self, validated_data):
        validated_data.pop('conf_password')
        user = Account.objects.create_user(**validated_data)
        return user
    

    def to_representation(self, instance):
        data= super().to_representation(instance)
        return {
            'msg': 'Account muvaffaqiyatli saqlandi',
            'user': data
        }  
#========================================================================

class LoginSerializer3(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        user = authenticate(username= username, password= password)
        if user is None:
            raise ValidationError('Username yoki parol xato')
        
        attrs['user'] = user
        return attrs
    
    def to_representation(self, instance):
        user  = instance['user']
        refresh_token = RefreshToken.for_user(user)
        return {
            "refresh_token": str(refresh_token),
            "access_token": str(refresh_token.access_token)
        }

#=============================================================


class ProfileSerializer3(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Account
        fields = ['id', 'username', 'first_name', 'last_name']


#==============================================================


class UpdateSerializer3(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Account
        fields = ['id', 'username', 'first_name', 'last_name']

#==============================================================


class PasswordChangeSerializer3(serializers.Serializer):
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


        
        
        
        
    

        