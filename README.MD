## 🚀 Visão Geral do Projeto

A **LojaVirtual** é uma aplicação web de e-commerce completa desenvolvida em **Django** e **Python**, com um frontend responsivo construído com **HTML**, **CSS** e **Bootstrap 4**. Este projeto foi criado com o objetivo de demonstrar habilidades sólidas em desenvolvimento web full-stack, cobrindo desde a gestão de banco de dados e lógica de backend até a interface de usuário interativa.

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
  * Funcionalidade de **Solicitar Reembolso** em pedidos.

* **Autenticação com JWT (Token):**

  * Integração com o `djangorestframework-simplejwt`.
  * Possibilita login via API usando tokens de acesso e refresh.
  * Permite proteger rotas de API com autenticação JWT, ideal para futuros usos com frontend em React/Vue ou mobile apps.

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

1. **Clone o repositório:**

2. **Crie e ative um ambiente virtual:**

```bash
python -m venv venv

# Para Windows:
venv\Scripts\activate

# Para macOS/Linux:
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute as migrações do banco de dados:**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crie um superusuário (para acesso ao painel administrativo):**

```bash
python manage.py createsuperuser
```

6. **Inicie o servidor de desenvolvimento:**

```bash
python manage.py runserver
```

## 💡 Como Usar

* Acesse a loja: `http://127.0.0.1:8000/`
* Explore produtos, adicione ao carrinho e finalize pedidos
* Registre-se ou faça login para testar funcionalidades exclusivas de usuários
* Admin: `http://127.0.0.1:8000/admin/`
* Teste o sistema de avaliações e solicitação de reembolso
* Teste o login via API JWT: `POST http://127.0.0.1:8000/api/token/`

## 📂 Estrutura do Projeto

├── LojaVirtual/  # Pasta raiz do projeto (ou ecommerce)
│   ├── accounts/  # Gerenciamento de usuários e autenticação
│   ├── cart/  # Lógica do carrinho de compras
│   ├── ecommerce\_project/  # Configurações globais do projeto
│   ├── orders/  # Gerenciamento de pedidos
│   ├── store/  # Produtos e funcionalidades principais da loja
│   ├── media/  # Upload de imagens
│   ├── static/  # Arquivos estáticos
│   ├── venv/  # Ambiente virtual
│   ├── db.sqlite3  # Banco de dados
│   ├── manage.py  # CLI do Django
│   └── requirements.txt
└── README.md

## 📸 Screenshots

* Página Inicial: screenshots\01 produtos.png
* Detalhes do Produto: screenshots\02 comentarios e avaliações.png
* Criar conta: screenshots\03 criar conta.png
* Login: screenshots\04 login.png
* Carrinho: screenshots\05 carrinho de compras.png
* Checkout: screenshots\10 finalizar pedido.png
* Simulação pagamento: screenshots\06 simulação de pagamento.png
* Pedido feito: screenshots\07 pedido realizado.png
* Solicitar Reembolso: screenshots\08 solicitar reembolso.png
* Reembolso feito: screenshots\09 reembolso feito.png

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar PRs.

## 🧑‍💻 Autor

**Lucas Gabriel**

* GitHub: [https://github.com/Lucasgsr08](https://github.com/Lucasgsr08)
* LinkedIn: [https://www.linkedin.com/in/lucas-gabriel-ramos-459151292/](https://www.linkedin.com/in/lucas-gabriel-ramos-459151292/)
