# Projeto ZipCode

API REST simples para interagir com o serviço do [Postmon](http://postmon.com.br) e salvar os dados relacionados a determinado CEP numa base sqlite.

## Setup

Para executar o serviço da API é necessário clonar o repositório do projeto e no diretório do projeto executar o seguinte comando:

`caminho_do_projeto: $ make setup`

Este comando configura um virtualenv com Python 2.7, instala as bibliotecas necessárias para execução do projeto e inicializa o banco de dados sqlite em `zipcode/zipcode.db`.

## Cobertura de testes

Existem 2 métodos no Makefile referentes aos testes:

1. `make test` para rodar os testes unitários;

2. `make coverage` para rodar os testes unitários com coverage;


## Executar app

Para executar o projeto basta executar o seguinte comando no diretório do projeto:

`caminho_do_projeto: $ make run`

Com esse comando o projeto estará acessível no endereço `http://localhost:5000/`

## Ações da API

### Inclusão

Busca detalhes do CEP informado no serviço do Postmon e salva na base local.

`POST /zipcode/`

Parâmetros:

* zip_code -> o CEP (somente números)

HTTP Code em caso de sucesso: 201

### Listagem

Busca os CEPs já inseridos na base local e os exibe numa listagem

`GET /zipcode/`

Parâmetros:

* limit (opcional) -> indica um limite para a listagem de registros

HTTP Code em caso de sucesso: 200

### Exclusão

Remove o CEP informado da base local, caso exista.

`DELETE /zipcode/<zip_code>`

Parâmetros:

* limit (opcional) -> indica um limite para a listagem de registros

HTTP Code em caso de sucesso: 204


### Consulta

Exibe os detalhes de determinado CEP.

`GET /zipcode/<zip_code>/`


HTTP Code em caso de sucesso: 200