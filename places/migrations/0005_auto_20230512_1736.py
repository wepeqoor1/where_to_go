# Generated by Django 3.2.15 on 2023-05-12 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_image_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('position',)},
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True, verbose_name='Позиция картинки'),
        ),
    ]
