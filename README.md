# Flask Todo List API

## Descrição do Projeto

Uma aplicação de gerenciamento de tarefas (Todo List) construída com Flask, PostgreSQL, e Docker, oferecendo uma API RESTful completa para manipulação de tarefas.

## Funcionalidades

- Criação de tarefas
- Listagem de tarefas
- Atualização de tarefas
- Exclusão de tarefas
- Validação de dados
- Dockerização da aplicação
- Testes unitários

## Pré-requisitos

- Python 3.9+
- Docker
- Docker Compose
- PostgreSQL

## Tecnologias Utilizadas

- Flask
- SQLAlchemy
- PostgreSQL
- Docker
- Pytest
- Marshmallow

## Instalação e Configuração

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/todo-list-flask.git
cd todo-list-flask
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```
SECRET_KEY=sua-chave-secreta
DATABASE_URL=postgresql://todouser:todopass@postgres:5432/tododb
```

### 3. Construir e Iniciar os Containers

```bash
docker-compose build
docker-compose up -d
```

### 4. Inicializar Banco de Dados

```bash
docker-compose run app flask db init
docker-compose run app flask db migrate
docker-compose run app flask db upgrade
```

## Endpoints da API

### Listar Tarefas
- **GET** `/todos`
- Retorna todas as tarefas

### Criar Tarefa
- **POST** `/todos`
- Corpo da requisição:
  ```json
  {
    "title": "Minha Tarefa",
    "description": "Descrição da tarefa",
    "completed": false
  }
  ```

### Atualizar Tarefa
- **PUT** `/todos/<id>`
- Corpo da requisição:
  ```json
  {
    "title": "Tarefa Atualizada",
    "completed": true
  }
  ```

### Excluir Tarefa
- **DELETE** `/todos/<id>`

## Executar Testes

```bash
# Instalar dependências de desenvolvimento
pip install -r requirements-dev.txt

# Rodar testes
pytest tests/
```

## Estrutura do Projeto

```
todo-list-flask/
│
├── app/
│   ├── __init__.py      # Configuração do Flask
│   ├── models.py        # Modelos de dados
│   ├── routes.py        # Rotas da API
│   └── schemas.py       # Esquemas de validação
│
├── tests/               # Testes unitários
│   ├── conftest.py
│   ├── test_models.py
│   └── test_routes.py
│
├── docker/              # Configurações Docker
│   ├── app.dockerfile
│   └── postgres.dockerfile
│
├── requirements.txt     # Dependências de produção
├── requirements-dev.txt # Dependências de desenvolvimento
├── config.py            # Configurações gerais
├── run.py               # Ponto de entrada da aplicação
└── docker-compose.yml   # Configuração do Docker Compose
```

## Contribuição

1. Faça fork do projeto
2. Crie sua feature branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'feat: Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um novo Pull Request

## Licença

MIT License </br>
Copyright (c) 2024 Álvaro Filho </br>
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions: </br>
</br>
The above copyright notice and this permission notice shall be included in all</br>
copies or substantial portions of the Software.</br>
</br>
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contato

Álvaro Filho - alvarofilho.dev@gmail.com

Projeto Link: https://github.com/4lvarofilho/flask-todo-list.git
