from django.db import models


class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = '주문'
        verbose_name_plural = '주문들'
