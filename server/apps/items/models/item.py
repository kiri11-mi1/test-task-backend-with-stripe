from django.core.validators import MinValueValidator
from django.db import models
from decimal import Decimal


class Item(models.Model):
    name = models.CharField('Наименование', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=10,
        decimal_places=2,
        validators=(MinValueValidator(Decimal('0.01')),)
    )

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return f'Покупка {self.id}: {self.name}'
