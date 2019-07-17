from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.user.models import User, SocialUser
from apps.user.enums import SocialProvider


class SocialUserSerializer(serializers.Serializer):
    provider = serializers.ChoiceField(
        label='플랫폼',
        choices=SocialProvider.choices()
    )
    uid = serializers.CharField()
    email = serializers.EmailField(
        label='이메일',
        required=False
    )
    name = serializers.CharField(
        label='이름',
        required=False
    )
    nickname = serializers.CharField(
        label='닉네임',
        required=False
    )

    def is_register(self):
        social_user = SocialUser.objects.filter(
            uid=self.validated_data['uid'],
            user__is_active=True
        )
        return social_user.exists()

    def register(self):
        validated_data = self.validated_data

        email = validated_data['email']
        name = validated_data['name']
        nickname = validated_data['nickname']

        uid = validated_data['uid']
        provider = validated_data['provider']

        if email is None:
            validated_data.update({
                'email': '{}@{}.com'.format(
                    uid,
                    provider
                )
            })

        user = User.objects.create(**validated_data)

        social_user = SocialUser.objects.create({
            'user': user,
            'provider': provider,
            'uid': uid
        })

        return user

    def login(self):
        return SocialUser.objects.filter(
            uid=self.validated_data['uid']
        ).last().user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label="이메일"
    )
    password = serializers.CharField(
        label="비밀번호"
    )

    def login(self):
        user = authenticate(
            username=self.validated_data['email'],
            password=self.validated_data['password']
        )

        return user


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label="이메일"
    )
    password = serializers.CharField(
        label="비밀번호"
    )

    def validate(self, data):
        email = data.get('email')

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "이미 가입된 이메일입니다."
            )
        return data

    def save(self):
        user = User(
            email=self.validated_data['email']
        )
        user.set_password(self.validated_data['password'])
        user.save()

        return user


class DuplicateSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def is_duplicate(self):
        return User.objects.filter(
            email=self.validated_data['email']
        ).exists()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
        ]
