from django.db import models


class Item(models.Model):
    name = models.CharField('Наименование', max_length=128)
    description = models.TextField('Описание')
    price = models.PositiveBigIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return f'Покупка {self.id}: {self.name}'
