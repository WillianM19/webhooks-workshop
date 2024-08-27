# Oficina - Webhooks

Este projeto é composto por dois servidores que gerenciam uma lista de livros e permitem adicionar e remover livros. O `book_server` gerencia a lista de livros e o `remove_book_server` lida com a remoção de livros, atualizando o `book_server` com a lista modificada.

## Estrutura do Projeto

- **`book_server.py`**: Servidor principal que gerencia a lista de livros.
- **`remove_book_server.py`**: Servidor que processa solicitações para remover livros da lista e atualiza o `book_server`.
- **`send_book.py`**: Cliente para enviar livros ao `book_server`.
- **`send_remove_book.py`**: Cliente para enviar solicitações de remoção ao `remove_book_server`.

## Instruções de Uso

### Configuração do Ambiente

1. Certifique-se de que o Python 3 e o `pip` estejam instalados em seu sistema.
2. Instale a biblioteca `requests` se ainda não estiver instalada:

   ```bash
   pip install requests
   ```

## Executando os Servidores

1. Inicie o book_server:

    ```bash
    python book_server.py
    ```
    O book_server estará escutando na porta 5000.

2. Inicie o remove_book_server:

    ```bash
    python remove_book_server.py
    ```
    O remove_book_server estará escutando na porta 5001.

4. Adicionando um Livro

    Para adicionar um livro ao book_server, use o script send_book.py. Exemplo:

    ```bash
    python send_book.py
    ```

5. Removendo um Livro

    Para remover um livro, use o script send_remove_book.py. Exemplo:

    ```bash
    python send_remove_book.py
    ```
