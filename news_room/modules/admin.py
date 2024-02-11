from django.contrib import admin
from modules.models import Menu, Block
from adminsortable2.admin import SortableAdminMixin


admin.site.register(Block)

@admin.register(Menu)
class SortableMenuAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'link', 'is_external', 'category', 'is_active')
    list_editable = ('link', 'is_external', 'category', 'is_active')

    ordering = ['name']