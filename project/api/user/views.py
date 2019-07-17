from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_jwt.settings import api_settings
from drf_yasg.utils import swagger_auto_schema

from apps.user.models import User
from .serializers import (
    LoginSerializer, SignUpSerializer,
    UserSerializer, SocialUserSerializer,
    DuplicateSerializer,
)
from .responses import (
    UserLoginSuccessResponse, UserLoginFailResponse,
    UserDuplicateResponse,
)


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


def generate_jwt_token(user):
    """
    유저 인스턴스를 통해 JWT 반환
    """
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    return token


class SocialUserAPIView(GenericAPIView):
    """
    소셜 로그인 API
    로그인 회원가입 구분없이 모두 한 API에서 처리
    """
    serializer_class = SocialUserSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="user_social",
        operation_summary="소셜 로그인 API",
        operation_descroption="소셜 유저 로그인. 로그인 시 JWT 반환",
        tags=['유저'],
        responses={
            '200': UserLoginSuccessResponse,
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not serializer.is_register():
            user = serializer.register()
        else:
            user = serializer.login()
        
        token = generate_jwt_token(user)

        return Response({
            'token': token
        })


class LoginAPIView(GenericAPIView):
    """
    이메일 로그인 API
    """
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="user_login",
        operation_summary="이메일 로그인 API",
        operation_description="유저 이메일 로그인. 로그인 시 JWT 반환",
        tags=['유저'],
        responses={
            '200': UserLoginSuccessResponse,
            '401': UserLoginFailResponse,
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.login()
        if user is None:
            return Response(
                UserLoginFailResponse.json(), 
                status=status.HTTP_401_UNAUTHORIZED
            )
            
        token = generate_jwt_token(user)

        return Response({
            'token': token
        })


class SignUpAPIView(GenericAPIView):
    """
    회원가입 API
    """
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="user_signup",
        operation_summary="이메일 회원가입 API",
        operation_description="유저 이메일 회원가입. 응답값으로 JWT 반환",
        tags=['유저'],
        responses={
            '201': UserLoginSuccessResponse,
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token = generate_jwt_token(user)

        return Response({
            token: 'token'
        }, status=status.HTTP_201_CREATED)


class DuplicateAPIView(GenericAPIView):
    serializer_class = DuplicateSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="user_duplicate",
        operation_summary="이메일 중복확인 API",
        operation_description="유저 이메일 중복확인.",
        tags=['유저'],
        responses={
            '200': UserDuplicateResponse,
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        is_duplicate = serializer.is_duplicate()

        return Response({
            'is_duplicate': is_duplicate
        })


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
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
