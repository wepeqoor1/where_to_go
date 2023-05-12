# Generated by Django 3.2.15 on 2023-05-12 19:46

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20230512_1736'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ('place_id',)},
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Длинное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=tinymce.models.HTMLField(blank=True, max_length=500, verbose_name='Краткое описание'),
        ),
    ]
