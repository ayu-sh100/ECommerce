from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django_otp.oath import TOTP
from django.utils.timezone import now

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Credentials")

class OTPLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    otp = serializers.CharField(write_only=True)

    def validate(self, data):
        user = User.objects.get(username=data['username'])
        device = user.otpdevice_set.first()  
        totp = TOTP(device.bin_key)
        if totp.verify(data['otp'], now()):
            return user
        raise serializers.ValidationError("Invalid OTP")