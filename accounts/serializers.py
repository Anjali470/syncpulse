from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["email", "username", "password", "first_name", "last_name",]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "username", "first_name", "last_name")
        read_only_fields = ("id", "email")

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def save(self):
        refresh_token = self.validated_data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()