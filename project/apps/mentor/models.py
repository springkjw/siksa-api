from django.db import models
from django.contrib.postgres.fields import ArrayField

from apps.user.models import User
from .enums import MentorCategory


class Mentor(models.Model):
    """
    멘토 모델
    """
    user = models.ForeignKey(
        User,
        verbose_name='유저',
        on_delete=models.CASCADE
    )

    public_phone_number = models.CharField(
        '공개 전화번호',
        max_length=11,
        null=True,
        blank=True
    )
    description = models.TextField(
        '소개',
        null=True,
        blank=True
    )
    category = ArrayField(
        models.SmallIntegerField(
            choices=MentorCategory.choices(),
        ),
        verbose_name='카테고리',
        help_text='복수 선택 가능'
    )

    is_active = models.BooleanField(
        '활성화 여부',
        default=True
    )

    class Meta:
        db_table = 'mentors'
        verbose_name = '멘토'
        verbose_name_plural = '멘토들'
