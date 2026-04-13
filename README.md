# BookStore API

API REST construída com Django e Django REST Framework para gerenciamento de livros, categorias e pedidos.

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

## Endpoints

Base URL: `http://localhost:8000/bookstore/v1/`

### Product

| Método | Endpoint              | Descrição               | Auth |
|--------|-----------------------|-------------------------|------|
| GET    | `/product/`           | Lista todos os produtos | Token |
| POST   | `/product/`           | Cria um produto         | Token |
| GET    | `/product/{id}/`      | Detalha um produto      | Token |
| DELETE | `/product/{id}/`      | Remove um produto       | Token |

### Category

| Método | Endpoint              | Descrição               | Auth |
|--------|-----------------------|-------------------------|------|
| GET    | `/category/`          | Lista todas as categorias | Não |
| POST   | `/category/`          | Cria uma categoria      | Não |
| GET    | `/category/{id}/`     | Detalha uma categoria   | Não |
| DELETE | `/category/{id}/`     | Remove uma categoria    | Não |

### Order

| Método | Endpoint          | Descrição           | Auth |
|--------|-------------------|---------------------|------|
| GET    | `/order/`         | Lista todos os pedidos | Não |
| POST   | `/order/`         | Cria um pedido      | Não |
| GET    | `/order/{id}/`    | Detalha um pedido   | Não |
| DELETE | `/order/{id}/`    | Remove um pedido    | Não |

### Autenticação

Os endpoints de produto exigem Token no header:

```
Authorization: Token <seu_token>
```

## Testes

```bash
# Rodar todos os testes
poetry run python manage.py test

# Rodar com output detalhado
poetry run python manage.py test --verbosity=2

# Rodar por app
poetry run python manage.py test product
poetry run python manage.py test order
```

### Cobertura dos testes

**product — viewsets**
- `test_get_all_products` — lista produtos paginados
- `test_get_product` — detalha produto por id
- `test_create_product` — cria produto com categoria
- `test_delete_product` — remove produto e confirma exclusão

**product — category viewset**
- `test_get_all_category` — lista categorias paginadas
- `test_create_category` — cria categoria e confirma no banco

**order — viewsets**
- `test_order` — lista pedidos com produtos e categorias aninhados
- `test_get_order` — detalha pedido por id
- `test_create_order` — cria pedido com produto e usuário
- `test_delete_order` — remove pedido e confirma exclusão
