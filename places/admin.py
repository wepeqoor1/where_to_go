from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.conf import settings

from .models import Place, Image


if settings.DEBUG:
    @admin.register(Image)
    class ImageAdmin(admin.ModelAdmin):
        list_display = ('image', 'image_preview', 'position')
        readonly_fields = ('image_preview',)


class ImageInlineAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    list_display = ('image', 'image_preview', 'position')
    readonly_fields = ('image_preview',)
    extra = 1
    ordering = ('position',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (ImageInlineAdmin,)
    list_display = ('title',)
    search_fields = ('title',)
