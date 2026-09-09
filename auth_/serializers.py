from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only = True)
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'first_name', 'last_name']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()