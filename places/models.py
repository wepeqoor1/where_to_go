from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    place_id = models.CharField(max_length=50, verbose_name='Идентификатор места')
    type = models.CharField(max_length=20, verbose_name='Тип')
    geometry_type = models.CharField(max_length=20, verbose_name='Тип фигуры на карте')
    longitude = models.FloatField(max_length=10, verbose_name='Долгота')
    latitude = models.FloatField(max_length=10, verbose_name='Широта')
    details_url = models.CharField(max_length=300, verbose_name='Путь до описания')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title
