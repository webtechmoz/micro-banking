# MicroBank

MicroBank é uma aplicação de simulação bancária desenvolvida com o framework Flet. Permite aos usuários simular diversas condições financeiras e acessar diferentes funcionalidades relacionadas à gestão bancária.

## Descrição

A aplicação MicroBank oferece um simulador bancário, onde os usuários podem testar diferentes condições financeiras. A interface é responsiva e ajusta-se automaticamente ao tamanho da janela.

## Instalação

Para instalar e executar o MicroBank localmente, siga os passos abaixo:

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/webtechmoz/micro-banking.git
    cd MicroBank
    ```

2. **Crie um ambiente virtual:**

    ```bash
    python -m venv venv
    ```

3. **Ative o ambiente virtual:**

    - No Windows:

        ```bash
        venv\Scripts\activate
        ```

    - No macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Execute a aplicação:**

    ```bash
    python main.py
    ```

## Uso

Após iniciar a aplicação, você pode acessar diferentes rotas para utilizar as funcionalidades:

- **Home:** `/`
- **Simulador:** `/simulator`
- **Página de erro:** `/error404`

A aplicação irá ajustar-se automaticamente ao tamanho da janela do navegador.

## Contribuição

Se deseja contribuir com o projeto, siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature: `git checkout -b feature/nova-feature`
3. Commit suas alterações: `git commit -m 'Adiciona nova feature'`
4. Push para a branch: `git push origin feature/nova-feature`
5. Envie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.