## Tecnologias Utilizadas

- **Python**: Linguagem principal da aplicação.
- **Quart**: Framework assíncrono baseado no Flask.
- **Quart-Auth**: Quart-Auth is an extension for Quart to provide for secure cookie authentication (session management).
- **Quart-Schema**: Quart-Schema is a Quart extension that provides schema validation and auto-generated API documentation.
- **Tortoise-ORM**: ORM para gerenciar as interações com o banco de dados.
- **Aerich**: Aerich is a database migrations tool for TortoiseORM, which is like alembic for SQLAlchemy, or like Django ORM with it's own migration solution.
- **PostgreSQL**: Banco de dados relacional.
- **Docker**: Ferramenta de contêinerização para facilitar o deployment e a execução da aplicação.

### Instalação

#### Rodando Localmente

1. Crie um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Inicie a aplicação:

   ```bash
   python run.py
   ```

#### Rodando com Docker

1. Construa a imagem Docker:

   ```bash
   docker-compose build
   ```

2. Inicie os contêineres:

   ```bash
   docker-compose up -d
   ```

### Migrações

Para executar as migrações do banco de dados, utilize os seguintes comandos:

```bash
docker exec -it <container_id> /bin/sh
aerich init -t app.database.config.TORTOISE_ORM
aerich init-db
aerich migrate
aerich update
```

### Documentação

Link para estrutura de:

- [Modelos](app\docs\models\README.md)
- [Repositórios](app\docs\repositories\README.md)
- [Rotas](app\docs\routes\README.md)
- [Esquemas](app\docs\schemas\README.md)
- [Serializadores](app\docs\serializers\README.md)
- [Serviços](app\docs\services\README.md)
- [Utilitários](app\docs\utils\README.md)

### Testes

**REST Client** (extensao):
1. Instale a extensao "REST Client" no vscode
   adicione no settings.json
   ```json
   "rest-client.environmentVariables": {
     "$shared": {
        "prodToken": "foo",
        "nonProdToken": "bar",
      },
     "local": {
        "version": "v1",
        "host": "localhost",
        "port": "5000",
        "token": "{{$shared nonProdToken}}",
        "secretKey": "dev-secret"
     },
     "production": {
        "host": "example.com", // teca-coif.com.br
        "token": "{{$shared prodToken}}",
        "secretKey" : "prodSecret"
     }
   },
   ```
   Em seguida mude para o environment Local

2. Na pasta ./tests/rest-client esta os .http para realizar as chamadas nos endpoints

<!-- Para executar os testes locais, após o início da aplicação, acesse: [SwaggerUI](http://localhost:5000/swaggerui/) -->

---
