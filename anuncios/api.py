# from ninja import NinjaAPI
# from ninja.security import django_auth
# from django.contrib.auth import authenticate, login, logout
# from django.middleware.csrf import get_token
# from .models import *
# from typing import List
# from django.shortcuts import get_object_or_404
# from .schemas import *

# api = NinjaAPI()

# # --- CRUD PARA REGIÃO ---
# @api.get("/regioes/", response=List[RegiaoSchema])S
# def listar_regioes(request):
#     return Regiao.objects.all()

# @api.post("/regioes", response=RegiaoSchema)
# def criar_regiao(request, data: RegiaoCreateSchema):
#     regiao = Regiao.objects.create(**data.dict())
#     return regiao

# @api.get("/regioes/{regiao_id}", response=RegiaoSchema)
# def obter_regiao(request, regiao_id: int):
#     regiao = get_object_or_404(Regiao, id=regiao_id)
#     return regiao

# @api.put("/regioes/{regiao_id}", response=RegiaoSchema)
# def atualizar_regiao(request, regiao_id: int, data: RegiaoCreateSchema):
#     regiao = get_object_or_404(Regiao, id=regiao_id)
#     for attr, value in data.dict().items():
#         setattr(regiao, attr, value)
#     regiao.save()
#     return regiao

# @api.delete("/regioes/{regiao_id}")
# def deletar_regiao(request, regiao_id: int):
#     regiao = get_object_or_404(Regiao, id=regiao_id)
#     regiao.delete()
#     return {"message": "Região deletada com sucesso"}

# # --- CRUD PARA PROVÍNCIA ---
# @api.get("/provincias", response=List[ProvinciaSchema])
# def listar_provincias(request):
#     return Provincia.objects.all()

# @api.post("/provincias", response=ProvinciaSchema)
# def criar_provincia(request, data: ProvinciaCreateSchema):
#     provincia = Provincia.objects.create(**data.dict())
#     return provincia

# @api.get("/provincias/{provincia_id}", response=ProvinciaSchema)
# def obter_provincia(request, provincia_id: int):
#     provincia = get_object_or_404(Provincia, id=provincia_id)
#     return provincia

# @api.put("/provincias/{provincia_id}", response=ProvinciaSchema)
# def atualizar_provincia(request, provincia_id: int, data: ProvinciaCreateSchema):
#     provincia = get_object_or_404(Provincia, id=provincia_id)
#     for attr, value in data.dict().items():
#         setattr(provincia, attr, value)
#     provincia.save()
#     return provincia

# @api.delete("/provincias/{provincia_id}")
# def deletar_provincia(request, provincia_id: int):
#     provincia = get_object_or_404(Provincia, id=provincia_id)
#     provincia.delete()
#     return {"message": "Província deletada com sucesso"}

# # --- CRUD PARA DISTRITO ---
# @api.get("/distritos", response=List[DistritoSchema])
# def listar_distritos(request):
#     return Distrito.objects.all()

# @api.post("/distritos", response=DistritoSchema)
# def criar_distrito(request, data: DistritoCreateSchema):
#     distrito = Distrito.objects.create(**data.dict())
#     return distrito

# @api.get("/distritos/{distrito_id}", response=DistritoSchema)
# def obter_distrito(request, distrito_id: int):
#     distrito = get_object_or_404(Distrito, id=distrito_id)
#     return distrito

# @api.put("/distritos/{distrito_id}", response=DistritoSchema)
# def atualizar_distrito(request, distrito_id: int, data: DistritoCreateSchema):
#     distrito = get_object_or_404(Distrito, id=distrito_id)
#     for attr, value in data.dict().items():
#         setattr(distrito, attr, value)
#     distrito.save()
#     return distrito

# @api.delete("/distritos/{distrito_id}")
# def deletar_distrito(request, distrito_id: int):
#     distrito = get_object_or_404(Distrito, id=distrito_id)
#     distrito.delete()
#     return {"message": "Distrito deletado com sucesso"}

# # --- CRUD PARA LOCALIDADE ---
# @api.get("/localidades", response=List[LocalidadeSchema])
# def listar_localidades(request):
#     return Localidade.objects.all()

# @api.post("/localidades", response=LocalidadeSchema)
# def criar_localidade(request, data: LocalidadeCreateSchema):
#     localidade = Localidade.objects.create(**data.dict())
#     return localidade

# @api.get("/localidades/{localidade_id}", response=LocalidadeSchema)
# def obter_localidade(request, localidade_id: int):
#     localidade = get_object_or_404(Localidade, id=localidade_id)
#     return localidade

# @api.put("/localidades/{localidade_id}", response=LocalidadeSchema)
# def atualizar_localidade(request, localidade_id: int, data: LocalidadeCreateSchema):
#     localidade = get_object_or_404(Localidade, id=localidade_id)
#     for attr, value in data.dict().items():
#         setattr(localidade, attr, value)
#     localidade.save()
#     return localidade

# @api.delete("/localidades/{localidade_id}")
# def deletar_localidade(request, localidade_id: int):
#     localidade = get_object_or_404(Localidade, id=localidade_id)
#     localidade.delete()
#     return {"message": "Localidade deletada com sucesso"}
