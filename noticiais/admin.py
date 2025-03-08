from django.contrib import admin
from .models import *

@admin.register(Blog)
class RegiaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    search_fields = ('titulo',)