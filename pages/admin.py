from django.contrib import admin
from .models import Page

# Configuracion extra

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'create_at')
    ordering = ('-create_at',)

# Register your models here.

admin.site.register(Page, PageAdmin)

# Configuracion del Panel

title = "Panel de Gestion"
subtitle = "Proyecto con Django"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle


