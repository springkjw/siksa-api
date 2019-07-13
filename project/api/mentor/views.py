from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from apps.mentor.models import Mentor
from .serializers import (
    MentorListSerializer,
)


class MentorViewSet(ModelViewSet):
    serializer_class = MentorListSerializer
    queryset = Mentor.objects.all()
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="mentor_create",
        operation_summary="멘토 생성",
        operation_description="멘토 생성",
        tags=['멘토'],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="mentor_list",
        operation_summary="멘토 리스트",
        operation_description="멘토 리스트",
        tags=['멘토'],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="mentor_retrieve",
        operation_summary="멘토 조회",
        operation_description="멘토 조회",
        tags=['멘토'],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="mentor_update",
        operation_summary="멘토 업데이트",
        operation_description="멘토 업데이트",
        tags=['멘토'],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="mentor_partial_update",
        operation_summary="멘토 부분 업데이트",
        operation_description="멘토 부분 업데이트",
        tags=['멘토'],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="mentor_destroy",
        operation_summary="멘토 삭제",
        operation_description="멘토 삭제",
        tags=['멘토'],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
