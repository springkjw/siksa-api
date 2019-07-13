from django.db import models


class FirstRegion(models.Model):
    """
    큰 지역 단위 모델
    """
    name = models.CharField(
        '지역명',
        max_length=20
    )

    class Meta:
        db_table = 'region_first'
        verbose_name = '큰 지역'
        verbose_name_plural = '큰 지역들'

    def __str__(self):
        return self.name


class SecondRegion(models.Model):
    """
    작은 지역 단위 모델 
    """
    first_region = models.ForeignKey(
        FirstRegion,
        verbose_name='큰 지역',
        on_delete=models.CASCADE
    )
    name = mdoels.CharField(
        '지역명',
        max_length=20
    )

    class Meta:
        db_table = 'region_second'
        verbose_name = '작은 지역'
        verbose_name_plural = '작은 지역들'

    def __str__(self):
        return self.name
