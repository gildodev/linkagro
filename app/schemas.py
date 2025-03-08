from ninja import Schema
from typing import List, Optional
from pydantic import BaseModel, HttpUrl


# Schema para Região
class RegiaoSchema(Schema):
    id: int
    regiao: str


class RegiaoCreateSchema(Schema):
    regiao: str

# Schema para Província
class ProvinciaSchema(Schema):
    id: int
    provincia: str
    regiao_id: int

class ProvinciaCreateSchema(Schema):
    provincia: str
    regiao_id: int

# Schema para Distrito
class DistritoSchema(Schema):
    id: int
    distrito: str
    provincia_id: int

class DistritoCreateSchema(Schema):
    distrito: str
    provincia_id: int

# Schema para Localidade
class LocalidadeSchema(Schema):
    id: int
    localidade: str
    distrito_id: int

class LocalidadeCreateSchema(Schema):
    localidade: str
    distrito_id: int


class ProdutoSchema(BaseModel):
    id: int
    nome_produto: str
    slug_produto: str


class ProdutorSchema(BaseModel):
    id: int
    nome_empresa: str
    user: int


class GaleriaVariedadeSchema(BaseModel):
    imagem_variedade: str
    default: bool



class VariedadeSchema(BaseModel):
    id: int
    nome_variedade: str
    produto_associado: ProdutoSchema
    id_produto_associado: int
    produtor_associado: ProdutorSchema
    id_produtor_associado: int
    detalhes_link: str
    unidade_variedade: str
    qualidade_variedade: str
    imagem_default: str
    galeria_variedade: List[GaleriaVariedadeSchema]
    descricao_variedade: str
    preco_por_unidade: str
    estoque_variedade: int
    quantidade_variedade: int
    id_regiao: int
    id_provincia: int
    provincia: str
    id_distrito: int
    distrito: str
    id_localidade: int
    localidade: str
    epoca_de_colheita: str
    data_inicio_colheita: str
    data_fim_colheita: str

    class Config:
        from_attributes=True
        # orm_mode = True  # Permite que os modelos ORM sejam automaticamente convertidos

