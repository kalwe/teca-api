# Models

Este diretório contém todos os modelos utilizados na aplicação. Os modelos são definidos utilizando o Tortoise-ORM e representam as tabelas do banco de dados.

## Estrutura dos Models

- `/shared/base_model.py`: Define o modelo base com campos compartilhados.
- `/shared/employee_related.py`: Define uma "FK" para associar.


## Como adicionar novos Models

1. Crie um novo arquivo Python no diretório `app/core/models`.
2. Defina a classe do modelo, herdando de `BaseModel`.
3. Adicione os campos necessários utilizando os tipos de campo do Tortoise-ORM.
4. Adicione o relacionamento com outros modelos, se necessário.
5. Atualize este README com a descrição do novo modelo.
