# Aplicativo de Gestão

Este é um aplicativo de gestão desenvolvido pelo aluno **Vinicius** para fins acadêmicos.

## Requisitos

- Python 3.x
- [venv](https://docs.python.org/3/library/venv.html) (ambiente virtual)
- [Django](https://www.djangoproject.com/)

## Instalação

1. Clone o repositório:
    ```bash
    git clone <url-do-repositorio>
    cd <nome-do-diretorio>
    ```

2. Crie o ambiente virtual:
    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    - **Windows:**
      ```bash
      venv\Scripts\activate
      ```
    - **Linux/Mac:**
      ```bash
      source venv/bin/activate
      ```

4. Instale o Django:
    ```bash
    pip install django
    ```

5. Rode as migrações e inicie o servidor:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

## Uso

Acesse `http://127.0.0.1:8000/` no navegador para utilizar o aplicativo.

---
Desenvolvido por Vinicius.# egestao
