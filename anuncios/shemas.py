from ninja import Schema
from typing import List, Optional

# Schema para Região
class BannerSchema(Schema):
    id: int
    tipo: str
    tiulo: str
    descricao: str
    mostrar_texto: bool
    activo: bool
    arquivo: str


# Schema para Província
class ParceirosSchema(Schema):
    id: int
    titulo: str
    arquivo: str
    mostrar_texto:bool


# Schema para Distrito
class ArmazenistaSchema(Schema):
    user_id:int
    nome:str
    sobrenome = str
    email = str
    empresa = str
    slogan = str
    username = str
    foto_perfil = str
    telefone = int
    telefone_2 = int
    provincia = int
    distrito = int
    localidade = int
    descricao = str
    activo=bool

class ArmazenistaCreateSchema(Schema):
    user_id:int
    foto_perfil = str
    empresa = str
    slogan = str
    telefone = int
    telefone_2 = int
    provincia = int
    distrito = int
    localidade = int
    descricao = str
    activo=bool

