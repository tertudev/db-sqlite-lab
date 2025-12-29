# 🧪 DB Sqlite Lab

Um projeto de laboratório para explorar e demonstrar operações CRUD básicas com bancos de dados SQLite em Python.

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

## 🧐 Sobre o Projeto

O `db-sqlite-lab` é um repositório de laboratório projetado para fornecer um exemplo prático e direto de como interagir com bancos de dados SQLite utilizando a linguagem Python. O objetivo principal é demonstrar as operações CRUD (Create, Read, Update, Delete) essenciais, que são a base para qualquer aplicação que manipule dados persistentes.

Este projeto utiliza o módulo `sqlite3` nativo do Python, que oferece uma interface compatível com DB-API 2.0 para bancos de dados SQLite. A implementação foca na clareza e na simplicidade, permitindo que desenvolvedores compreendam rapidamente os conceitos de conexão, execução de comandos SQL e gerenciamento de transações. O arquivo `my_bank.db` serve como um banco de dados de exemplo, simulando um cenário bancário simples para ilustrar a criação de contas e o registro de transações.

A abordagem técnica é direta, sem a introdução de ORMs complexos ou frameworks de alto nível, para que o foco permaneça na interação SQL pura e nos fundamentos da persistência de dados com SQLite.

## ✨ Funcionalidades

*   **Conexão e Gerenciamento:** Estabelece e gerencia a conexão com o banco de dados SQLite (`my_bank.db`).
*   **Criação de Esquema:** Demonstra a criação de tabelas (`accounts`, `transactions`) com tipos de dados apropriados.
*   **Inserção de Dados (Create):** Exemplifica a adição de novos registros, como a abertura de uma nova conta ou o registro de uma transação.
*   **Consulta de Dados (Read):** Permite a recuperação de informações, como o saldo de uma conta específica ou o histórico de transações.
*   **Atualização de Dados (Update):** Ilustra a modificação de registros existentes, como depósitos e saques em contas.
*   **Exclusão de Dados (Delete):** Apresenta a remoção de registros, como o encerramento de uma conta (para fins demonstrativos).
*   **Tratamento de Erros:** Inclui exemplos básicos de tratamento de exceções para operações de banco de dados.

## 🛠️ Tecnologias

As seguintes tecnologias foram utilizadas neste projeto:

*   **Python:** Linguagem de programação principal (versão 3.x).
*   **SQLite:** Sistema de gerenciamento de banco de dados leve e embarcado.
*   **`sqlite3`:** Módulo padrão do Python para interação com bancos de dados SQLite.

## 🚀 Como Começar

Para configurar e executar este projeto em sua máquina local, siga os passos abaixo.

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado em seu sistema.

*   [Python 3.x](https://www.python.org/downloads/)

### Instalação

Não há dependências externas a serem instaladas além da biblioteca padrão do Python.

1.  Clone o repositório:
    ```bash
    git clone https://github.com/tertudev/db-sqlite-lab.git
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd db-sqlite-lab
    ```

### Execução

Para executar o script e observar as operações de banco de dados:

```bash
python labproject.py
```

Ao executar o `labproject.py`, o script irá:
1.  Conectar-se ao banco de dados `my_bank.db` (ou criá-lo se não existir).
2.  Criar as tabelas `accounts` e `transactions`.
3.  Inserir dados de exemplo.
4.  Realizar operações de consulta, atualização e exclusão.
5.  Imprimir os resultados no console.

## 📂 Estrutura

A estrutura do repositório é simples e direta:

```
.
├── .gitignore         # Arquivo para ignorar arquivos e diretórios específicos do controle de versão.
├── LICENSE            # Licença do projeto (MIT).
├── README.md          # Este arquivo de documentação.
├── labproject.py      # Script Python principal com a lógica de interação com o SQLite.
└── my_bank.db         # Arquivo do banco de dados SQLite gerado e manipulado pelo script.
```

## 🤝 Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou quiser corrigir algum problema, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

Vamos codar o futuro! 🚀
