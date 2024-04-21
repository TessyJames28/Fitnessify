from rest_framework import serializers
from .models import UserRegistration
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['username', 'email', 'password']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Customize the payload as per your requirements
        token = super().get_token(user)
        # Add custom claims to the token payload if needed
        # token['custom_claim'] = 'value'
        return token


from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
