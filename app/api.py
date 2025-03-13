from ninja import NinjaAPI
from ninja.security import django_auth
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from .models import *
from typing import List, Optional
from django.shortcuts import get_object_or_404
from .schemas import *
from rest_framework.reverse import reverse
from django.utils import timezone
from datetime import timedelta
from ninja.pagination import paginate, PageNumberPagination
from django.core.paginator import Paginator
from django.db.models import Q


api = NinjaAPI()

# --- CRUD PARA REGIÃO ---
@api.get("/regioes/", response=List[RegiaoSchema])
def listar_regioes(request):
    return Regiao.objects.all()

@api.post("/regioes", response=RegiaoSchema)
def criar_regiao(request, data: RegiaoCreateSchema):
    regiao = Regiao.objects.create(**data.dict())
    return regiao

@api.get("/regioes/{regiao_id}", response=RegiaoSchema)
def obter_regiao(request, regiao_id: int):
    regiao = get_object_or_404(Regiao, id=regiao_id)
    return regiao

@api.put("/regioes/{regiao_id}", response=RegiaoSchema)
def atualizar_regiao(request, regiao_id: int, data: RegiaoCreateSchema):
    regiao = get_object_or_404(Regiao, id=regiao_id)
    for attr, value in data.dict().items():
        setattr(regiao, attr, value)
    regiao.save()
    return regiao

@api.delete("/regioes/{regiao_id}")
def deletar_regiao(request, regiao_id: int):
    regiao = get_object_or_404(Regiao, id=regiao_id)
    regiao.delete()
    return {"message": "Região deletada com sucesso"}

# --- CRUD PARA PROVÍNCIA ---
@api.get("/provincias", response=List[ProvinciaSchema])
def listar_provincias(request):
    return Provincia.objects.all()

@api.post("/provincias", response=ProvinciaSchema)
def criar_provincia(request, data: ProvinciaCreateSchema):
    provincia = Provincia.objects.create(**data.dict())
    return provincia

@api.get("/provincias/{provincia_id}", response=ProvinciaSchema)
def obter_provincia(request, provincia_id: int):
    provincia = get_object_or_404(Provincia, id=provincia_id)
    return provincia

@api.put("/provincias/{provincia_id}", response=ProvinciaSchema)
def atualizar_provincia(request, provincia_id: int, data: ProvinciaCreateSchema):
    provincia = get_object_or_404(Provincia, id=provincia_id)
    for attr, value in data.dict().items():
        setattr(provincia, attr, value)
    provincia.save()
    return provincia

@api.delete("/provincias/{provincia_id}")
def deletar_provincia(request, provincia_id: int):
    provincia = get_object_or_404(Provincia, id=provincia_id)
    provincia.delete()
    return {"message": "Província deletada com sucesso"}

# --- CRUD PARA DISTRITO ---
@api.get("/distritos", response=List[DistritoSchema])
def listar_distritos(request):
    return Distrito.objects.all()

@api.post("/distritos", response=DistritoSchema)
def criar_distrito(request, data: DistritoCreateSchema):
    distrito = Distrito.objects.create(**data.dict())
    return distrito

@api.get("/distritos/{distrito_id}", response=DistritoSchema)
def obter_distrito(request, distrito_id: int):
    distrito = get_object_or_404(Distrito, id=distrito_id)
    return distrito

@api.put("/distritos/{distrito_id}", response=DistritoSchema)
def atualizar_distrito(request, distrito_id: int, data: DistritoCreateSchema):
    distrito = get_object_or_404(Distrito, id=distrito_id)
    for attr, value in data.dict().items():
        setattr(distrito, attr, value)
    distrito.save()
    return distrito

@api.delete("/distritos/{distrito_id}")
def deletar_distrito(request, distrito_id: int):
    distrito = get_object_or_404(Distrito, id=distrito_id)
    distrito.delete()
    return {"message": "Distrito deletado com sucesso"}

# --- CRUD PARA LOCALIDADE ---
@api.get("/localidades", response=List[LocalidadeSchema])
def listar_localidades(request):
    return Localidade.objects.all()

@api.post("/localidades", response=LocalidadeSchema)
def criar_localidade(request, data: LocalidadeCreateSchema):
    localidade = Localidade.objects.create(**data.dict())
    return localidade

@api.get("/localidades/{localidade_id}", response=LocalidadeSchema)
def obter_localidade(request, localidade_id: int):
    localidade = get_object_or_404(Localidade, id=localidade_id)
    return localidade

@api.put("/localidades/{localidade_id}", response=LocalidadeSchema)
def atualizar_localidade(request, localidade_id: int, data: LocalidadeCreateSchema):
    localidade = get_object_or_404(Localidade, id=localidade_id)
    for attr, value in data.dict().items():
        setattr(localidade, attr, value)
    localidade.save()
    return localidade

@api.delete("/localidades/{localidade_id}")
def deletar_localidade(request, localidade_id: int):
    localidade = get_object_or_404(Localidade, id=localidade_id)
    localidade.delete()
    return {"message": "Localidade deletada com sucesso"}


# todos os produtos da categoria
@api.get("produtos-categoria/{slug_categoria}/")
def get_produto_categoria(request, slug_categoria: str, page: int = 1, periodo: int=1):
    # Obter o produto com base no slug_produto
    categoria = get_object_or_404(Categoria, slug_categoria=slug_categoria)
    # Definindo a data atual
    data_atual = timezone.now().date()

    # Filtrar as variedades com base nas condições
    variedades_ativas = Variedade.objects.filter(
        produto_variedade__categoria_produto=categoria,
        activo=True
    )

    # Aplicando os filtros corretamente
    variedades_ativas = variedades_ativas.filter(data_inicio_colheita__lte=data_atual, data_fim_colheita__gte=data_atual) if periodo == 1 else variedades_ativas.filter(data_inicio_colheita__gt=data_atual).order_by("data_inicio_colheita")

    # Cria um Paginator com 10 veículos por página
    paginator = Paginator(variedades_ativas, 1)
    
    # Obtém a página solicitada
    pagina = paginator.get_page(page)

    variedades_lista_activa=[]

    for variedade in pagina:
        variedades_lista_activa.append(
            {
                "id": variedade.id,
                "nome_variedade": variedade.nome_variedade,
                "produto_associado": {
                    "id": variedade.produto_variedade.id,
                    "nome_produto": variedade.produto_variedade.nome_produto,
                    "slug_produto": variedade.produto_variedade.slug_produto
                },
                "id_produto_associado": variedade.produto_variedade.id,
                "produtor_associado": {
                    "id": variedade.produtor_variedade.id,
                    "nome_empresa": variedade.produtor_variedade.nome_empresa or "",  # Se estiver vazio, passa uma string vazia
                    "user": variedade.produtor_variedade.user.id
                },

                "id_produtor_associado": variedade.produtor_variedade.id,
                "detalhes_link":  reverse('linkagro_detalhe_variedade', kwargs={'varied': variedade.slug_variedade}, request=request),
                "imagem_default": variedade.imagem_variedade().url if variedade.imagem_variedade else None,

                "galeria_variedade": [
                    {"imagem_variedade": img.imagem_variedade.url, "default": img.default}
                    for img in variedade.variedade_galerias.all()
                ],
                "descricao_variedade": variedade.descricao_variedade,
                "preco_por_unidade": str(variedade.preco_por_unidade),
                "unidade_variedade": variedade.unidade_variedade,
                "estoque_variedade": variedade.estoque_variedade,
                "quantidade_variedade": variedade.quantidade_variedade,
                "qualidade_variedade": variedade.qualidade,
                "epoca_de_colheita": variedade.epoca_de_colheita,
                "data_inicio_colheita": variedade.data_inicio_colheita.isoformat(),
                "data_fim_colheita": variedade.data_fim_colheita.isoformat(),
                "id_regiao": variedade.provincia.regiao.pk,
                "id_provincia": variedade.provincia.id,
                "provincia": variedade.provincia.provincia,  # Assumindo que você tem uma relação com `provincia`
                "id_distrito": variedade.distrito.id,
                "distrito": variedade.distrito.distrito,
                "id_localidade": variedade.localidade.pk if variedade.localidade else 0,
                "localidade": variedade.localidade.localidade if variedade.localidade else "",
            }
        )

    # Criar a resposta com todos os dados
    return {
        "variedades_activas": [VariedadeSchema.from_orm(variedade) for variedade in variedades_lista_activa], 
        "total_produtos": paginator.count,  # Total de veículos
        "pagina_actual": pagina.number,  # Página atual
        "total_paginas": paginator.num_pages,  # Total de páginas
        "proxima_pagina": pagina.next_page_number() if pagina.has_next() else False,
        "pagina_anterior": pagina.previous_page_number() if pagina.has_previous() else False,
        "ha_proxima_pagina": pagina.has_next(),  # Se há próxima página
        "ha_pagina_anterior": pagina.has_previous(),  # Se há página anterior
        "periodo": periodo,
    }


# proxima colheita
@api.get("produtos-categoria/{slug_categoria}/proximas-colheitas/")
def get_produto_categoria_proximas_colheitas(request, slug_categoria: str):
    # Obter o produto com base no slug_produto
    categoria = get_object_or_404(Categoria, slug_categoria=slug_categoria)
    # Definindo a data atual
    data_atual = timezone.now().date()


    variedades_proximas_colheita = Variedade.objects.filter(
        produto_variedade__categoria_produto=categoria,
        activo=True,
        data_inicio_colheita__gt=data_atual  # Variedades com colheita começando após a data atual
    ).order_by("data_inicio_colheita") 


    variedades_lista_proxima_colheita=[]
    

    for variedade in variedades_proximas_colheita:
        
        variedades_lista_proxima_colheita.append(
            {
                "id": variedade.id,
                "nome_variedade": variedade.nome_variedade,
                "produto_associado": {
                    "id": variedade.produto_variedade.id,
                    "nome_produto": variedade.produto_variedade.nome_produto,
                    "slug_produto": variedade.produto_variedade.slug_produto
                },
                "id_produto_associado": variedade.produto_variedade.id,
                "produtor_associado": {
                    "id": variedade.produtor_variedade.id,
                    "nome_empresa": variedade.produtor_variedade.nome_empresa or "",  # Se estiver vazio, passa uma string vazia
                    "user": variedade.produtor_variedade.user.id
                },

                "id_produtor_associado": variedade.produtor_variedade.id,
                "detalhes_link":  reverse('linkagro_detalhe_variedade', kwargs={'varied': variedade.slug_variedade}, request=request),
                "imagem_default": variedade.imagem_variedade().url if variedade.imagem_variedade else None,

                "galeria_variedade": [
                    {"imagem_variedade": img.imagem_variedade.url, "default": img.default}
                    for img in variedade.variedade_galerias.all()
                ],
                "descricao_variedade": variedade.descricao_variedade,
                "preco_por_unidade": str(variedade.preco_por_unidade),
                "unidade_variedade": variedade.unidade_variedade,
                "estoque_variedade": variedade.estoque_variedade,
                "quantidade_variedade": variedade.quantidade_variedade,
                "qualidade_variedade": variedade.qualidade,
                "epoca_de_colheita": variedade.epoca_de_colheita,
                "data_inicio_colheita": variedade.data_inicio_colheita.isoformat(),
                "data_fim_colheita": variedade.data_fim_colheita.isoformat(),
                "id_regiao": variedade.provincia.regiao.pk,
                "id_provincia": variedade.provincia.id,
                "provincia": variedade.provincia.provincia,  # Assumindo que você tem uma relação com `provincia`
                "id_distrito": variedade.distrito.id,
                "distrito": variedade.distrito.distrito,
                "id_localidade": variedade.localidade.pk if variedade.localidade else 0,
                "localidade": variedade.localidade.localidade if variedade.localidade else "",
            }
        )

    # Criar a resposta com todos os dados
    return {
        "variedades_proximas_colheitas": [VariedadeSchema.from_orm(variedade) for variedade in variedades_lista_proxima_colheita],
    }



# Variedades de produtos
@api.get("variedades-produto/{slug_produto}/")
def get_produto_varirdades(request, slug_produto: str, page: int = 1, periodo: int=1):

    # Definindo a data atual
    data_atual = timezone.now().date()

    # Obter o produto com base no slug_produto
    produto = get_object_or_404(Produto, slug_produto=slug_produto)

    
    variedades_ativas = Variedade.objects.filter(
        produto_variedade=produto,
        activo=True
    )

    # Aplicando os filtros corretamente
    variedades_ativas = variedades_ativas.filter(data_inicio_colheita__lte=data_atual, data_fim_colheita__gte=data_atual) if periodo == 1 else variedades_ativas.filter(data_inicio_colheita__gt=data_atual).order_by("data_inicio_colheita")


    # Cria um Paginator com 10 veículos por página
    paginator = Paginator(variedades_ativas, 1)
    
    # Obtém a página solicitada
    pagina = paginator.get_page(page)

    variedades=[]
    

    for variedade in pagina:
        
        variedades.append(
            {
                "id": variedade.id,
                "nome_variedade": variedade.nome_variedade,
                "produto_associado": {
                    "id": variedade.produto_variedade.id,
                    "nome_produto": variedade.produto_variedade.nome_produto,
                    "slug_produto": variedade.produto_variedade.slug_produto
                },
                "id_produto_associado": variedade.produto_variedade.id,
                "produtor_associado": {
                    "id": variedade.produtor_variedade.id,
                    "nome_empresa": variedade.produtor_variedade.nome_empresa or "",  # Se estiver vazio, passa uma string vazia
                    "user": variedade.produtor_variedade.user.id
                },

                "id_produtor_associado": variedade.produtor_variedade.id,
                "detalhes_link":  reverse('linkagro_detalhe_variedade', kwargs={'varied': variedade.slug_variedade}, request=request),
                "imagem_default": variedade.imagem_variedade().url if variedade.imagem_variedade else None,

                "galeria_variedade": [
                    {"imagem_variedade": img.imagem_variedade.url, "default": img.default}
                    for img in variedade.variedade_galerias.all()
                ],
                "descricao_variedade": variedade.descricao_variedade,
                "preco_por_unidade": str(variedade.preco_por_unidade),
                "unidade_variedade": variedade.unidade_variedade,
                "estoque_variedade": variedade.estoque_variedade,
                "quantidade_variedade": variedade.quantidade_variedade,
                "qualidade_variedade": variedade.qualidade,
                "epoca_de_colheita": variedade.epoca_de_colheita,
                "data_inicio_colheita": variedade.data_inicio_colheita.isoformat(),
                "data_fim_colheita": variedade.data_fim_colheita.isoformat(),
                "id_regiao": variedade.provincia.regiao.pk,
                "id_provincia": variedade.provincia.id,
                "provincia": variedade.provincia.provincia,  # Assumindo que você tem uma relação com `provincia`
                "id_distrito": variedade.distrito.id,
                "distrito": variedade.distrito.distrito,
                "id_localidade": variedade.localidade.pk if variedade.localidade else 0,
                "localidade": variedade.localidade.localidade if variedade.localidade else "",
            }
        )

    # Criar a resposta com todos os dados
    return {
        "variedades_activas": [VariedadeSchema.from_orm(variedade) for variedade in variedades], 
        "total_produtos": paginator.count,  # Total de veículos
        "pagina_actual": pagina.number,  # Página atual
        "total_paginas": paginator.num_pages,  # Total de páginas
        "proxima_pagina": pagina.next_page_number() if pagina.has_next() else False,
        "pagina_anterior": pagina.previous_page_number() if pagina.has_previous() else False,
        "ha_proxima_pagina": pagina.has_next(),  # Se há próxima página
        "ha_pagina_anterior": pagina.has_previous(),  # Se há página anterior
        "periodo": periodo,
    }


@api.get("enderecos-geograficos-produtores/")
def get_todos_enderecos_geograficos_produtores(request):

    # Obter todas as regiões, províncias, distritos e localidades
    regioes = Regiao.objects.all()
    provincias = Provincia.objects.all()
    distritos = Distrito.objects.all()
    localidades = Localidade.objects.all()
    
    # Criar a resposta com todos os dados
    return {
        "regioes": [RegiaoSchema.from_orm(regiao) for regiao in regioes],
        "provincias": [ProvinciaSchema.from_orm(provincia) for provincia in provincias],
        "distritos": [DistritoSchema.from_orm(distrito) for distrito in distritos],
        "localidades": [LocalidadeSchema.from_orm(localidade) for localidade in localidades],
    }


# Retornar produtos pesquisados
@api.get("pesquisa")
def pesquisar_variedades(
        request, 
        page: Optional[int] =1,
        periodo: Optional[int] =1,
        q: Optional[str] = None, 
        regiao: Optional[str] = None, 
        provincia: Optional[str] = None, 
        distrito: Optional[str] = None
    ):
    
    # Definindo a data atual
    data_atual = timezone.now().date()

    variedades_ativas = Variedade.objects.filter(activo=True)

    # Aplicando os filtros corretamente
    variedades_ativas = variedades_ativas.filter(data_inicio_colheita__lte=data_atual, data_fim_colheita__gte=data_atual) if periodo == 1 else variedades_ativas.filter(data_inicio_colheita__gt=data_atual).order_by("data_inicio_colheita")

    if q:
        variedades_ativas = variedades_ativas.filter(nome_variedade__icontains=q)
    if regiao:
        variedades_ativas = variedades_ativas.filter(provincia__regiao__pk=regiao)
    if provincia:
        variedades_ativas = variedades_ativas.filter(provincia__pk=provincia)
    if distrito:
        variedades_ativas = variedades_ativas.filter(distrito__pk=distrito)


    # Cria um Paginator com 10 veículos por página
    paginator = Paginator(variedades_ativas, 1)
    
    # Obtém a página solicitada
    pagina = paginator.get_page(page)

    variedades_lista_activa=[]


    for variedade in pagina:
        
        variedades_lista_activa.append(
            {
                "id": variedade.id,
                "nome_variedade": variedade.nome_variedade,
                "produto_associado": {
                    "id": variedade.produto_variedade.id,
                    "nome_produto": variedade.produto_variedade.nome_produto,
                    "slug_produto": variedade.produto_variedade.slug_produto
                },
                "id_produto_associado": variedade.produto_variedade.id,
                "produtor_associado": {
                    "id": variedade.produtor_variedade.id,
                    "nome_empresa": variedade.produtor_variedade.nome_empresa or "",  # Se estiver vazio, passa uma string vazia
                    "user": variedade.produtor_variedade.user.id
                },

                "id_produtor_associado": variedade.produtor_variedade.id,
                "detalhes_link":  reverse('linkagro_detalhe_variedade', kwargs={'varied': variedade.slug_variedade}, request=request),
                "imagem_default": variedade.imagem_variedade().url if variedade.imagem_variedade else None,

                "galeria_variedade": [
                    {"imagem_variedade": img.imagem_variedade.url, "default": img.default}
                    for img in variedade.variedade_galerias.all()
                ],
                "descricao_variedade": variedade.descricao_variedade,
                "preco_por_unidade": str(variedade.preco_por_unidade),
                "unidade_variedade": variedade.unidade_variedade,
                "estoque_variedade": variedade.estoque_variedade,
                "quantidade_variedade": variedade.quantidade_variedade,
                "qualidade_variedade": variedade.qualidade,
                "epoca_de_colheita": variedade.epoca_de_colheita,
                "data_inicio_colheita": variedade.data_inicio_colheita.isoformat(),
                "data_fim_colheita": variedade.data_fim_colheita.isoformat(),
                "id_regiao": variedade.provincia.regiao.pk,
                "id_provincia": variedade.provincia.id,
                "provincia": variedade.provincia.provincia,  # Assumindo que você tem uma relação com `provincia`
                "id_distrito": variedade.distrito.id,
                "distrito": variedade.distrito.distrito,
                "id_localidade": variedade.localidade.pk if variedade.localidade else 0,
                "localidade": variedade.localidade.localidade if variedade.localidade else "",
            }
        )

    # Criar a resposta com todos os dados
    return {
        "variedades_activas": [VariedadeSchema.from_orm(variedade) for variedade in variedades_lista_activa], 
        "total_produtos": paginator.count,  # Total de veículos
        "pagina_actual": pagina.number,  # Página atual
        "total_paginas": paginator.num_pages,  # Total de páginas
        "proxima_pagina": pagina.next_page_number() if pagina.has_next() else False,
        "pagina_anterior": pagina.previous_page_number() if pagina.has_previous() else False,
        "ha_proxima_pagina": pagina.has_next(),  # Se há próxima página
        "ha_pagina_anterior": pagina.has_previous(),  # Se há página anterior
    }





