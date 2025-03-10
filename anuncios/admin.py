from django.contrib import admin
from .models import *

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    search_fields = ('titulo',)

@admin.register(Parceiros)
class ParceirosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', )
    search_fields = ('titulo',)
    list_filter = ('titulo',)

@admin.register(Armazem)
class ArmazemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_armazem', 'armazenista', 'provincia', 'distrito', 'disponivel')
    search_fields = ('nome_armazem', 'armazenista__user__username')
    list_filter = ('provincia', 'distrito', 'disponivel')

@admin.register(GaleriaArmazem)
class GaleriaArmazemAdmin(admin.ModelAdmin):
    list_display = ('id', 'armazem_galeria', 'imagem_armazem', 'activo')
    list_filter = ('activo',)




