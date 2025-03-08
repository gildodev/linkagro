from django.contrib import admin
from .models import *
from django.utils.html import format_html


@admin.register(Regiao)
class RegiaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'regiao')
    search_fields = ('regiao',)

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'provincia', 'regiao')
    search_fields = ('provincia',)
    list_filter = ('regiao',)

@admin.register(Distrito)
class DistritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'distrito', 'provincia')
    search_fields = ('diistrito',)
    list_filter = ('provincia',)

@admin.register(Localidade)
class LocalidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'localidade', 'distrito')
    search_fields = ('localidade',)
    list_filter = ('distrito',)

@admin.register(Produtor)
class ProdutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'telefone','tipo_produtor', 'activo')
    search_fields = ('user__username', 'telefone')
    list_filter = ( 'activo', 'provincia')
    readonly_fields = ('data_cadastro',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'imagem_variedade_thumbnail', 'nome_categoria', 'activo')
    search_fields = ('nome_categoria',)
    prepopulated_fields = {'slug_categoria': ('nome_categoria',)}
    list_filter = ('activo',)
    editable=('activo')

    # Função para renderizar a imagem no admin
    def imagem_variedade_thumbnail(self, obj):
        if obj.imagem_categoria:
            # Cria uma miniatura da imagem para exibir no admin
            return format_html('<img src="{}" style="border-radius: 1rem;" width="30" height="30" />', obj.imagem_categoria.url)
        return "Sem imagem"

    # Adiciona a função no list_display e usa o método imagem_variedade_thumbnail para exibir a imagem
    imagem_variedade_thumbnail.allow_tags = True  # Permite renderizar HTML (importante!)
    imagem_variedade_thumbnail.short_description = 'Imagem'  # Define o título da coluna


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id','imagem_variedade_thumbnail', 'nome_produto', "categoria_produto", "variedades_activas", "proximas_colhetas", "numero_variedades" ,'data_adicionado')
    search_fields = ('nome_produto', 'produtor_produto__user__username')
    list_filter = ('categoria_produto', 'data_adicionado')

    # Função para renderizar a imagem no admin
    def imagem_variedade_thumbnail(self, obj):
        if obj.imagem_produto:
            # Cria uma miniatura da imagem para exibir no admin
            return format_html('<img src="{}" style="border-radius: 1rem;" width="30" height="30" />', obj.imagem_produto.url)
        return "Sem imagem"
    
     # Adiciona a função no list_display e usa o método imagem_variedade_thumbnail para exibir a imagem
    imagem_variedade_thumbnail.allow_tags = True  # Permite renderizar HTML (importante!)
    imagem_variedade_thumbnail.short_description = 'Imagem'  # Define o título da coluna


@admin.register(Variedade)
class VariedadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto_variedade', 'nome_variedade', 'preco_por_unidade', 'produtor_variedade', 'estoque_variedade', 'epoca_de_colheita')
    search_fields = ('nome_variedade', 'produto_variedade__nome_produto')
    list_filter = ('epoca_de_colheita', 'qualidade')
    prepopulated_fields = {'slug_variedade': ('nome_variedade',)}

@admin.register(GaleriaVariedade)
class VariedadeGaleriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'variedade_galeria', 'default', 'activo',)
    search_fields = ('variedade_galeria',)
    list_filter = ('variedade_galeria',)