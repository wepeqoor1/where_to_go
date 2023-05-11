from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Place, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'image_preview', 'position')
    readonly_fields = ('image_preview',)


class ImageInline(admin.TabularInline):
    model = Image
    list_display = ('image', 'image_preview', 'position')
    readonly_fields = ('image_preview',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)
