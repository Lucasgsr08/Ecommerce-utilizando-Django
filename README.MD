🚀 Visão Geral do Projeto



A **LojaVirtual** é uma aplicação web de e-commerce completa desenvolvida em **Django** e **Python**, com um frontend responsivo construído com **HTML**, **CSS** e **Bootstrap 4**. Este projeto foi criado com o objetivo de demonstrar habilidades sólidas em desenvolvimento web full-stack, cobrindo desde a gestão de banco de dados e lógica de backend até a interface de usuário interativa. É um excelente exemplo de aplicação para um portfólio técnico.



## ✨ Funcionalidades Principais



O sistema LojaVirtual oferece uma gama robusta de funcionalidades para uma experiência de compra online eficiente:



* **Catálogo de Produtos:**

    * Listagem dinâmica de produtos com imagens, nomes e preços.

    * Página de detalhes do produto com descrição completa, status de disponibilidade e opção de adicionar ao carrinho.

    * Sistema de busca e filtragem por preço.

* **Carrinho de Compras Interativo:**

    * Adição, remoção e atualização de quantidades de produtos no carrinho.

    * Exibição clara de subtotais e total do pedido.

    * Persistência dos itens do carrinho via sessão do usuário.

* **Autenticação e Gerenciamento de Usuários:**

    * Registro de novos usuários.

    * Login e Logout seguros.

* **Avaliações e Comentários de Produtos:**

    * Sistema de avaliação por estrelas (1 a 5) nos detalhes do produto.

    * Funcionalidade para usuários autenticados deixarem comentários e classificações sobre os produtos.

    * Exibição da média de avaliação e contagem total de avaliações.

* **Processo de Pedidos:**

    * Finalização de compra com formulário para dados do cliente (endereço, etc.).

    * Histórico de pedidos para usuários logados.

    * Detalhes de pedidos individuais.

    * Funcionalidade de **Solicitar Reembolso** em pedidos .

* **Administração Poderosa (Django Admin):**

    * Interface administrativa completa para gerenciamento de:

        * Produtos e Categorias

        * Pedidos e Itens de Pedido

        * Carrinhos (se necessário para debug/gerenciamento)

        * Comentários de Produtos

    * Permite controle total sobre o conteúdo da loja.

* **Gerenciamento de Mídia:**

    * Upload e exibição de imagens de produtos.



## 🛠️ Tecnologias Utilizadas



* **Backend:**

    * [Python](https://www.python.org/) (Versão recomendada: 3.11+)

    * [Django](https://www.djangoproject.com/) (Versão: 5.2.3)

* **Frontend:**

    * HTML5

    * CSS3

    * [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) (Versão: 4.x - via `crispy-bootstrap4`)

    * [Font Awesome](https://fontawesome.com/) (para ícones como carrinho, estrelas)

* **Banco de Dados:**

    * [SQLite3](https://www.sqlite.org/index.html) (Padrão do Django, leve e ideal para desenvolvimento local)

* **Gerenciamento de Pacotes:**

    * [pip](https://pip.pypa.io/en/stable/)

* **Ambiente Virtual:**

    * [venv](https://docs.python.org/3/library/venv.html)







## 🚀 Como Rodar o Projeto Localmente



Siga os passos abaixo para configurar e executar a LojaVirtual em seu ambiente de desenvolvimento:



1.  **Clone o repositório:**

    ```bash

    git clone <URL_DO_SEU_REPOSITORIO>

    cd LojaVirtual # ou o nome da sua pasta raiz do projeto (ex: ecommerce)

    ```

    *(Substitua `<URL_DO_SEU_REPOSITORIO>` pelo link do seu GitHub/GitLab/Bitbucket)*



2.  **Crie e ative um ambiente virtual:**

    ```bash

    python -m venv venv

    # Para Windows:

    venv\Scripts\activate

    # Para macOS/Linux:

    source venv/bin/activate

    ```



3.  **Instale as dependências:**

    ```bash

    pip install -r requirements.txt

    ```



4.  **Execute as migrações do banco de dados:**

    ```bash

    python manage.py makemigrations

    python manage.py migrate

    ```



5.  **Crie um superusuário (para acesso ao painel administrativo):**

    ```bash

    python manage.py createsuperuser

    ```

    Siga as instruções no terminal para definir nome de usuário, e-mail e senha.



6.  **Inicie o servidor de desenvolvimento:**

    ```bash

    python manage.py runserver

    ```



## 💡 Como Usar



Após iniciar o servidor, a aplicação estará disponível em seu navegador.



* **Acesse a Loja:** Abra seu navegador e vá para `http://127.0.0.1:8000/`.

* **Navegue e Compre:** Explore os produtos, adicione-os ao carrinho e experimente o processo de checkout.

* **Autenticação:**

    * **Registre-se:** Crie uma nova conta de usuário para testar as funcionalidades de usuário logado (carrinho persistente, histórico de pedidos, comentários).

    * **Faça Login:** Use suas credenciais para acessar seu perfil.

* **Painel Administrativo:** Acesse `http://127.0.0.1:8000/admin/` e faça login com as credenciais do superusuário que você criou. Explore a interface para gerenciar produtos, usuários, pedidos e muito mais.

* **Teste o Sistema de Avaliações:** Faça login e adicione comentários e classificações aos produtos.

* **Teste a Funcionalidade de Reembolso:** Se um pedido tiver o botão "Solicitar Reembolso", clique para ver o fluxo (ou explique no README se for apenas um status visível para o usuário e gerenciado pelo admin).



## 📂 Estrutura do Projeto



A estrutura do projeto está organizada em módulos Django para manter a clareza e a modularidade:

├── LojaVirtual/                # Pasta raiz do projeto (ou ecommerce)

│   ├── accounts/             # Gerenciamento de usuários e autenticação

│   ├── cart/                 # Lógica do carrinho de compras

│   ├── ecommerce_project/    # Configurações globais do projeto (settings, urls)

│   ├── orders/               # Gerenciamento de pedidos

│   ├── store/                # Produtos, categorias e funcionalidades principais da loja

│   ├── media/                # Diretório para upload de imagens (ex: imagens de produtos)

│   ├── static/               # Arquivos estáticos (CSS, JavaScript, Imagens do tema)

│   ├── venv/                 # Ambiente virtual do Python

│   ├── db.sqlite3            # Banco de dados SQLite

│   ├── manage.py             # Utilitário de linha de comando do Django

│   └── requirements.txt      # Dependências do projeto

└── README.md                 # Este arquivo





## 📸 Screenshots



* **Página Inicial/Listagem de Produtos:** screenshots\01 produtos.png  

* **Detalhes do Produto com Avaliações:** screenshots\02 comentarios e avaliaçoes.png

* **Criar conta:** screenshots\03 criar conta.png

* **Página do Carrinho:** screenshots\05 carrinho de compras.png

* **Página de Checkout:** screenshots\10 finalizar pedido.png

* **simulaçao de pagamento:** screenshots\06 simulaçao de pagamento.png

* **pedido realizado:** screenshots\07 pedido realizado.png

* **Página de Login/Registro:** screenshots\04 login.png

* **solicitar reembolso:**screenshots\08 solicitar reembolso.png

* **reembolso feito:**screenshots\09 reembolso feito.png







## 🤝 Contribuições



Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou enviar pull requests.





## 🧑‍💻 Autor



**Lucas Gabriel**

* [GitHub]: https://github.com/Lucasgsr08

* [LinkedIn]: https://www.linkedin.com/in/lucas-gabriel-ramos-459151292/