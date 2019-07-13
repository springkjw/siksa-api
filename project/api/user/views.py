from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from apps.user.models import User
from .serializers import (
    LoginSerializer, SignUpSerializer,
    UserSerializer,
)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="user_login",
        operation_summary="이메일 로그인 API",
        operation_description="유저 이메일 로그인. 로그인 시 JWT 반환",
        tags=['유저'],
        responses={
            '200': LoginSerializer
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response()


class SignUpAPIView(GenericAPIView):
    # 회원가입 API
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="user_signup",
        operation_summary="이메일 회원가입 API",
        operation_description="유저 이메일 회원가입. 응답값으로 JWT 반환",
        tags=['유저'],
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_id="user_create",
        operation_summary="유저 생성",
        operation_description="유저 생성",
        tags=['유저'],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="user_list",
        operation_summary="유저 리스트",
        operation_description="유저 리스트",
        tags=['유저'],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="user_retrieve",
        operation_summary="유저 조회",
        operation_description="유저 조회",
        tags=['유저'],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="user_update",
        operation_summary="유저 업데이트",
        operation_description="유저 업데이트",
        tags=['유저'],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="user_partial_update",
        operation_summary="유저 부분 업데이트",
        operation_description="유저 부분 업데이트",
        tags=['유저'],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="user_destroy",
        operation_summary="유저 삭제",
        operation_description="유저 삭제",
        tags=['유저'],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
