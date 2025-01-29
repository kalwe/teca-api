# Repositórios

Este diretório contém todos os repositórios utilizados na aplicação. Os repositórios são responsáveis por interagir com o banco de dados e realizar operações CRUD nas entidades,

## Estrutura dos Repositórios

- `additional_repository.py`: Define o repositório para a entidade Additional.
- `address_repository.py`: Define o repositório para a entidade Address.
- `attachment_repository.py`: Define o repositório para a entidade Attachment.
- `contact_repository.py`: Define o repositório para a entidade Contact.
- `contract_repository.py`: Define o repositório para a entidade Contract.
- `general_information_repository.py`: Define o repositório para a entidade GeneralInformation.
- `item_repository.py`: Define o repositório para a entidade Item.
- `organization_client_repository.py`: Define o repositório para a entidade OrganizationClient.
- `reassignment_repository.py`: Define o repositório para a entidade Reassignment.
- `role_repository.py`: Define o repositório para a entidade Role.
- `sei_repository.py`: Define o repositório para a entidade SEI.
- `unions_repository.py`: Define o repositório para a entidade Union.

## Como adicionar novos Repositórios

1. Crie um novo arquivo Python no diretório `app/repositories`.
2. Defina a classe do repositório, herdando de `BaseRepository` ou implementando a interface correspondente.
3. Implemente os métodos necessários para realizar operações CRUD na entidade.
4. Atualize este README com a descrição do novo repositório.
