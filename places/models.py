from django.db import models
from django.utils.html import format_html


class Place(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    place_id = models.CharField(max_length=50, verbose_name='Идентификатор места')
    type = models.CharField(max_length=20, verbose_name='Тип')
    geometry_type = models.CharField(max_length=20, verbose_name='Тип фигуры на карте')
    longitude = models.FloatField(max_length=10, verbose_name='Долгота')
    latitude = models.FloatField(max_length=10, verbose_name='Широта')
    details_url = models.CharField(max_length=300, verbose_name='Путь до описания')
    description_short = models.CharField(max_length=500, blank=True, verbose_name='Краткое описание')
    description_long = models.TextField(blank=True, verbose_name='Длинное описание')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.id}. {self.title}'


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Место')
    image = models.ImageField(upload_to='places/', verbose_name='Ссылка на изображение')
    position = models.IntegerField(blank=True, null=True, verbose_name='Позиция картинки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')

    def image_preview(self):
        return format_html('<img src="{}" width="100" />'.format(self.image.url))

    image_preview.short_description = 'Изображение'

    def __str__(self):
        return f'{self.id}. {self.place.title}'
