# kabum_api
## Descrição do Projeto 📘
Este projeto consiste em uma API REST desenvolvida para a KaBuM!, um dos maiores e-commerces de tecnologia da América Latina. A API fornece cotações de fretes com base nas dimensões e peso dos produtos, consultando diferentes opções de transportadoras.

O sistema foi projetado para receber requisições POST com detalhes do produto e retornar uma lista de opções de frete disponíveis, juntamente com seus custos e prazos estimados de entrega.

## Tech Stack 🛠️
* **Flask:** Um micro-framework web escrito em Python, usado para construir a API REST.
* **Docker:** Uma plataforma de contêineres que facilita a implantação e execução da aplicação em ambientes isolados.
* **Docker Compose:** Uma ferramenta para definir e gerenciar aplicações multi-contêineres com Docker.
* **Python:** Linguagem de programação utilizada para desenvolver a lógica de negócios da aplicação.
* **Unittest:** Biblioteca do Python utilizada para a escrita de testes unitários do sistema.

## Instruções para Execução 🚀
Para executar e interagir com a API, siga as instruções abaixo. Certifique-se de ter o Docker e o Docker Compose instalados em seu sistema para as etapas que envolvem o uso de contêineres.

### Configuração Inicial
1. Clonagem do Repositório
   ```
      git clone git@github.com:JuniorGunner/kabum_test.git
      cd kabum_test
   ```

### Execução Direta (Sem Docker)
1. Iniciar a aplicação
   ```
      make run
   ```
A API estará acessível em http://localhost:5000.

2. Executar testes
   ```
      make test
   ```
3. Executar testes com output detalhado
   ```
      make test-verbose
   ```

### Execução com Docker
1. Construção da imagem
   ```
      make build
   ```
2. Iniciar a aplicação
   ```
      make run-docker
   ```
A API estará acessível em http://localhost:5000.

3. Parar a aplicação
   ```
      make stop
   ```

### Exemplo de request
![Screenshot from 2023-12-02 09-15-32](https://github.com/JuniorGunner/kabum_test/assets/12654382/6f36f374-9864-43e6-831f-af2e6d455917)
