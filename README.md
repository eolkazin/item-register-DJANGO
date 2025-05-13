# 🗂️ Sistema de Cadastro de Itens

Um sistema web para **gerenciamento de itens cadastrados**, com funcionalidades de **login**, **cadastro de novos itens**, **exclusão de itens**, e visualização detalhada de cada item. Construído com Django no back-end e HTML/CSS no front-end.

## 🚀 Funcionalidades

- **🔑 Login e Cadastro de Usuário**: Tela de login para usuários autenticados e cadastro para novos usuários.
- **📋 Lista de Itens Cadastrados**: Exibição de todos os itens cadastrados com detalhes como nome, preço, quantidade, localização, código e descrição.
- **➕ Cadastro de Novo Item**: Interface simples para adicionar novos itens, incluindo nome, preço, quantidade, localização, código, descrição e imagem.
- **🗑️ Deletar Itens**: Funcionalidade para excluir itens diretamente da lista.

## 🧑‍💻 Tecnologias Utilizadas

- **🐍 Django**: Framework back-end utilizado para o desenvolvimento da aplicação.
- **🌐 HTML5 e CSS3**: Para a construção do layout e estilo das páginas.
- **🖋️ FontAwesome**: Para ícones utilizados nas páginas.
- **⚙️ Django Template Language (DTL)**: Para renderizar dinamicamente o conteúdo na interface.

## 🛠️ Como Rodar o Projeto

### Requisitos

- Python 3.x
- Django 4.x
- Banco de Dados (SQLite, PostgreSQL, etc.)

### Passo 1: Clone o Repositório

```bash
git clone https://github.com/seu-usuario/projeto.git
```
```
cd projeto
```
### Passo 2: Instale as Dependências
- Crie um ambiente virtual e instale as dependências:

```
python -m venv venv
source venv/bin/activate  # No Windows use venv\Scripts\activate
pip install -r requirements.txt
```

### Passo 3: Configure o Banco de Dados
- Realize as migrações para configurar o banco de dados:

```

python manage.py migrate
Passo 4: Inicie o Servidor
python manage.py runserver
```

Agora, abra o navegador e acesse o endereço http://127.0.0.1:8000/ para visualizar a aplicação.

## 📝 Como Funciona

1. ## 🔒 Tela de Login
A tela de login permite que o usuário acesse a aplicação com suas credenciais. Se o usuário não estiver cadastrado, pode se registrar e criar uma nova conta.

2. ## 📜 Lista de Itens Cadastrados
A tela principal exibe todos os itens cadastrados com as seguintes informações:

🛍️ Nome

💲 Preço

🔢 Quantidade

📍 Localização

🔑 Código

📖 Descrição

Se o item tiver uma imagem associada, ela será exibida também.

3. ## ➕ Tela de Cadastro de Itens
A tela de cadastro permite que os usuários registrem novos itens fornecendo as seguintes informações:

📝 Nome

💲 Preço

🔢 Quantidade

📍 Localização

🔑 Código

📖 Descrição

🖼️ Imagem (opcional)

4. ## 🗑️ Deletar Item
Cada item possui um botão de deletar. Ao clicar no botão, o item será removido da base de dados permanentemente.

### 🤝 Contribuições
Contribuições são muito bem-vindas! Se você deseja ajudar a melhorar o projeto ou corrigir bugs, fique à vontade para criar uma Pull Request.

- **Faça o fork do repositório.**

- **Crie uma branch com a sua feature: git checkout -b minha-feature.**

- **Comite suas mudanças: git commit -am 'Adiciona nova feature'.**

- **Envie para o repositório remoto: git push origin minha-feature.**

- **Abra uma Pull Request.**

📜 Licença
- Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

Desenvolvido com ❤️ por **Lucas Guerra**
