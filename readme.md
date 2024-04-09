# Python Technical Challenge

## Pré-requisitos

- **Docker**: versão 24.0.7 ou superior

## Instalação e Execução

1. **Clonar o repositório:**

   ```bash
   git clone git@github.com:Abraao-Andrade/python-technical-challenge.git

2. **Acessar o repositório:**

    ```bash
    cd python-technical-challenge

3. **Construa a imagem Docker usando o Dockerfile fornecido:**
    ```bash
    docker build -t test-python .

4. **Iniciar o contêiner Docker com a imagem recém-criada:**
    ```bash
    docker run -d -p 8000:8000 test-python


## Endpoints

*   `/orders/combine_orders`: Faz o cálculo do número mínimo de viagens, dadas umas lista de requisições.
*   `/contracts/get_top_n_open_contracts`: Retorna os N maiores devedores que ainda não possuem seus débitos renegociados.
*   `/batch/`: Endpoint criado para aceitar requisições em lote.
*   `http://0.0.0.0:8000/docs`: Todos os endpoints podem ser testados e explorados utilizando a interface interativa.