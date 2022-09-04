# Graphsql Study

Projeto para estudo sobre o GraphQL.

O projeto consiste em um API para cadastro de livros (title / author) onde é inserida em um banco de dados Sqlite para
possível consulta atraves do GraphQL.

-- -

### 📋 Pré-requisitos

#### 1 - Instalar Poetry:

https://python-poetry.org/docs/#installation

#### 2 - Permitir criação virtual env local

```
poetry config virtualenvs.in-project true
```

#### 3 - Criação virtual env

```
poetry shell
```

-- -

### 🔧 Instalação

Instalação dependencias

```
poetry install
```

📋 CLI (Command-line Interface)

```
poetry run api
```

-- -

### 📋 Requests

Cadastrar um novo livro
```
curl --location --request POST 'http://localhost:6010/books' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Senhor dos Aneis",
    "author": "victor"
}'
```

Buscar todos os livros cadastrados
```
curl --location --request GET 'http://localhost:6010/books'
```

Deletar um livro

```
curl --location --request DELETE 'http://localhost:6010/books/1'
```

GraphQL query (http://localhost:6010/graphql)

```
{
    books {
        title
        author
    }
}
```

-- -

### 🔧 Deploy

utilizar o commitzen para commit

```
cz commit
```

-- -

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [strawberry](https://strawberry.rocks/) - Strawberry is a new GraphQL library for Python 3, inspired by dataclasses.
* [graphql](https://graphql.org/) - A query language for your API
* [fastapi](https://fastapi.tiangolo.com/) - FastAPI framework
* [sqlite](https://www.sqlite.org/index.html) - Database

-- -

## ✒️ Autores

* **Victor Augusto Barros** - - [VictorAugustoBarros](https://github.com/VictorAugustoBarros)
