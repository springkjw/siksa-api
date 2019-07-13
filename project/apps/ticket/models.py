from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField

from utils.models import GenericDatetimeModel
from apps.mentor.models import Mentor


class Ticket(GenericDatetimeModel):
    mentor = models.ForeignKey(
        Mentor,
        verbose_name='멘토',
        null=True,
        on_delete=models.SET_NULL
    )

    sale_period = DateTimeRangeField(
        '판매 기간'
    )

    is_active = models.BooleanField(
        '활성화 여부',
        default=False
    )

    class Meta:
        db_table = 'tickets'
        verbose_name = '티켓'
        verbose_name_plural = '티켓들'


class TicketOption(GenericDatetimeModel):
    ticket = models.ForeignKey(
        Ticket,
        verbose_name='티켓',
        on_delete=models.CASCADE
    )
    # name = 