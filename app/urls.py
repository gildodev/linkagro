from django.contrib import admin
from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    path('', linkagro.index, name="linkagro_home"),
    path('local-de-producao/', linkagro.pagina_de_informe_de_locais_de_producao, name="linkagro_local_producao"),
    path('categoria/<slug:categ>.html', linkagro.pagina_de_produtos_da_categoria, name="linkagro_produtos_categoria"),
    path('produtos/<slug:produto>.html', linkagro.pagina_de_variedades_de_produto, name="linkagro_variedade_produto"),
    path('detalhes-produto/<slug:varied>.html', linkagro.panina_de_detalhes_da_variedade, name="linkagro_detalhe_variedade"),
    path('noticias/', linkagro.panina_de_detalhes_da_variedade, name="linkagro_noticias"),
    path('noticia/<slug:noticia>.html', linkagro.panina_de_detalhes_da_variedade, name="linkagro_noticia"),
    path('pesquisa/?', linkagro.panina_de_pesquisa, name="linkagro_pesquisa"),
    path('anuncie-aqui/', linkagro.panina_de_anunciantes, name="linkagro_anuncie_aqui"),
    path('como-funciona/', linkagro.panina_como_funciona, name="linkagro_como_funciona"),
    path('termos-e-condicoes/', linkagro.panina_de_termos_condicoes, name="linkagro_termos_condicoes"),
    path('politicas-privacidade/', linkagro.panina_de_politica_privacidade, name="linkagro_politicas_privacidade"),

    path('api/', api.urls)
]
