from django.core.exceptions import (
    ValidationError, ObjectDoesNotExist, PermissionDenied, FieldError, SuspiciousOperation
)
from django.db import IntegrityError, DatabaseError, OperationalError, DataError, ProgrammingError
from django.http import Http404

# 🔹 Dicionário com Códigos de Status HTTP e Mensagens Padrão
HTTP_STATUS_CODES = {
    200: "OK - Solicitação bem-sucedida.",
    201: "Criado - O recurso foi criado com sucesso.",
    202: "Aceito - A solicitação foi aceita para processamento.",
    204: "Sem Conteúdo - A solicitação foi processada, mas não há conteúdo para retornar.",
    400: "Requisição Inválida - Os dados enviados são inválidos.",
    401: "Não Autorizado - Credenciais inválidas ou não fornecidas.",
    403: "Proibido - Você não tem permissão para acessar este recurso.",
    404: "Não Encontrado - O recurso solicitado não foi encontrado.",
    405: "Método Não Permitido - O método HTTP não é permitido para este endpoint.",
    409: "Conflito - Erro de integridade ou duplicação de dados.",
    422: "Entidade Não Processável - Os dados enviados não podem ser processados.",
    429: "Muitas Solicitações - Você excedeu o limite de requisições.",
    500: "Erro Interno do Servidor - Um erro inesperado ocorreu.",
    502: "Bad Gateway - Erro ao se comunicar com um serviço externo.",
    503: "Serviço Indisponível - O servidor está temporariamente indisponível.",
    504: "Gateway Timeout - O tempo limite da requisição foi atingido."
}

def handle_django_exception(exc):
    """
    Captura exceções do Django e retorna um dicionário contendo:
    - Código de status HTTP
    - Mensagem de erro apropriada
    """
    
    # 🔹 ERROS DE VALIDAÇÃO & CLIENTE (400-499)
    if isinstance(exc, ValidationError):
        return {"status": 400, "error": exc.message_dict}
    elif isinstance(exc, ObjectDoesNotExist) or isinstance(exc, Http404):
        return {"status": 404, "error": HTTP_STATUS_CODES[404]}
    elif isinstance(exc, PermissionDenied):
        return {"status": 403, "error": HTTP_STATUS_CODES[403]}
    elif isinstance(exc, FieldError):
        return {"status": 400, "error": "Erro de campo inválido na consulta."}
    elif isinstance(exc, SuspiciousOperation):
        return {"status": 400, "error": HTTP_STATUS_CODES[400]}
    
    # 🔹 ERROS DE BANCO DE DADOS (500-599)
    elif isinstance(exc, IntegrityError):
        return {"status": 409, "error": HTTP_STATUS_CODES[409]}
    elif isinstance(exc, DatabaseError):
        return {"status": 500, "error": HTTP_STATUS_CODES[500]}
    elif isinstance(exc, OperationalError):
        return {"status": 503, "error": HTTP_STATUS_CODES[503]}
    elif isinstance(exc, DataError):
        return {"status": 400, "error": HTTP_STATUS_CODES[400]}
    elif isinstance(exc, ProgrammingError):
        return {"status": 500, "error": HTTP_STATUS_CODES[500]}

    # 🔹 ERROS NÃO TRATADOS
    else:
        return {"status": 500, "error": HTTP_STATUS_CODES[500]}
