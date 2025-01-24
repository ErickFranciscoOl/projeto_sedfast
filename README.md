# Projeto SEDFAST

Este projeto tem como objetivo a automação da coleta e enriquecimento de dados de empresas e seus sócios a partir de informações de CNPJ. Ele busca informações detalhadas sobre a empresa (como telefone, email, nome) e sobre os sócios, coletando dados como nome, telefone, email e LinkedIn.

## Funcionalidades

- **Buscar dados da empresa**: A partir de um CNPJ, busca as informações cadastrais da empresa, como nome, telefone e e-mail.
- **Buscar dados dos sócios**: Com o nome do sócio e da empresa, realiza uma consulta via API para encontrar informações como cargo, e-mail, telefone e LinkedIn dos sócios.
- **Enriquecimento de dados**: Através das APIs da Receita Federal e Apollo, são enriquecidas as informações da empresa e dos sócios.
- **Leitura e gravação de dados**: Lê os CNPJs de um arquivo CSV, realiza as consultas e grava os resultados em um arquivo Excel.

## Como Funciona

### 1. Leitura dos CNPJs

Os CNPJs são lidos de um arquivo CSV, e para cada CNPJ, são feitas as seguintes etapas:

- **Busca de informações da empresa**: A função `buscar_dados_cnpj` consulta a API da Receita Federal para obter os dados da empresa.
- **Busca de dados dos sócios**: Para cada sócio da empresa, a função `buscar_socio_apollo` é chamada para obter informações sobre os sócios a partir da API da Apollo.

### 2. Dados Extraídos

Os seguintes dados são extraídos e salvos:

- **Dados da empresa**:
  - Nome da empresa
  - Telefone da empresa
  - E-mail da empresa
- **Dados dos sócios**:
  - Nome do sócio
  - E-mail do sócio
  - Telefone do sócio
  - LinkedIn do sócio (caso disponível)

### 3. Resultado

Todos os dados extraídos são salvos em um arquivo Excel, com as informações organizadas para fácil visualização e análise.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `requests` (para fazer as requisições HTTP)
  - `pandas` (para manipulação de dados)
  - `openpyxl` (para salvar os dados no formato Excel)
- Uma chave de API da Apollo (`API_KEY`), necessária para realizar as buscas de sócios.

## Contribuindo

Se você quiser contribuir para o projeto, fique à vontade para enviar pull requests. Sinta-se à vontade para sugerir melhorias ou relatar problemas.
