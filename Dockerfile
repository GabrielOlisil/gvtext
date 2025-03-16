FROM python:3.12-alpine

# Instala o Poetry
ENV POETRY_VERSION=2.1.1
RUN pip install "poetry==$POETRY_VERSION"

# Define o diretório de trabalho
WORKDIR /app

# Copia o pyproject.toml e o poetry.lock
COPY pyproject.toml poetry.lock ./

# Instala as dependências
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# Copia o código
COPY . .

# Expõe a porta do Django
EXPOSE 8000

# Roda o servidor Django
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]