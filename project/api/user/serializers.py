from rest_framework import serializers
from apps.user.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label="이메일"
    )
    password = serializers.CharField(
        label="비밀번호"
    )


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label="이메일"
    )
    password = serializers.CharField(
        label="비밀번호"
    )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
        ]