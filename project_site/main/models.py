from django.db import models
from datetime import datetime
from django.utils import timezone



class Reviews(models.Model):
    name = models.CharField("ФИО", max_length=45, blank=True)
    review = models.CharField("Отзыв", max_length=300, blank=True)
    date = models.DateTimeField("Дата и время отзыва", blank=True)


    def __str__(self):
        return f'{self.name} {self.date}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Settings(models.Model):
    number = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='')
    mail = models.CharField(max_length=200)

    def __str__(self):
        return f'Контактные данные'

    class Meta:
        verbose_name = "Данные"
        verbose_name_plural = "Данные"
