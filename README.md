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
# Rodar todos os testes
poetry run python manage.py test

# Rodar com output detalhado
poetry run python manage.py test --verbosity=2

# Rodar por app
poetry run python manage.py test product
poetry run python manage.py test order

# Rodar uma classe específica
poetry run python manage.py test product.tests.CategorySerializerTest
poetry run python manage.py test product.tests.ProductSerializerTest
poetry run python manage.py test order.tests.OrderSerializerTest
```

### Cobertura dos testes

**product**
- `CategorySerializerTest` — valida campos e conteúdo do `CategorySerializer`
- `ProductSerializerTest` — valida campos, preço e category aninhado no `ProductSerializer`

**order**
- `OrderSerializerTest` — valida campos, product aninhado, cálculo do `total` com um e múltiplos produtos
