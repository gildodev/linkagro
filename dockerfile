FROM python:3.12-slim

# Instalar dependências do sistema necessárias para o mysqlclient
RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Configurar o ambiente Python
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copiar o código do projeto
COPY . /app/

# Instalar as dependências do Python
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Definir o comando de inicialização
CMD ["python", "manage.py", "runserver"]
