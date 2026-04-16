# BookStore API

API REST, construída com Django e Django REST Framework.

## Requisitos

- Python 3.12+
- Poetry

## Instalação

```bash
# Clone o repositório
git clone https://github.com/Reinaldo-Sn/bookstore1.git
cd d-bookstore

# Instale as dependências
poetry install

# Ative o ambiente virtual
poetry shell
```

## Configuração

```bash
# Rode as migrations
poetry run python manage.py migrate

# Crie um superusuário (opcional)
poetry run python manage.py createsuperuser
```

## Rodando o projeto

```bash
poetry run python manage.py runserver
```

Acesse em: http://localhost:8000

Painel admin: http://localhost:8000/admin

## Testes

```bash
pytest
```
