from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from authentication.models import User
from sample_app.models import Customer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSignUpSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True, write_only=True)
    username = serializers.CharField(max_length=100, required=True, write_only=True)
    confirm_password = serializers.CharField(max_length=128, required=True, write_only=True)
    password = serializers.CharField(max_length=128, required=True, write_only=True)

    class Meta:
        model = User
        fields = ['name', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        validated_data["password"] = make_password(validated_data["password"])
        user = User.objects.create(role='user', **validated_data)
        user.is_active = True
        user.save()
        return user

    def validate_password(self, password):
        validate_password(password)
        return password

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords don't match!")
        return data

class CustomerSignUpSerializer(UserSignUpSerializer):

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        validated_data["password"] = make_password(validated_data["password"])
        user = User.objects.create(role='customer', **validated_data)
        user.is_active = True
        user.save()
        Customer.objects.create(user=user)
        return user


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(max_length=200)