# Generated by Django 3.2.15 on 2023-05-10 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='description_long',
            field=models.TextField(blank=True, verbose_name='Длинное описание'),
        ),
        migrations.AddField(
            model_name='place',
            name='description_short',
            field=models.CharField(blank=True, max_length=500, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='places/', verbose_name='Ссылка на изображение'),
        ),
    ]
