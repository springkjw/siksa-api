from django.db import models


class GenericDatetimeModel(models.Model):
    """
    생성일과 수정일 추상화 모델
    """
    created = models.DateTimeField(
        '생성일',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        '수정일',
        auto_now=True
    )

    class Meta:
        abstract = True
