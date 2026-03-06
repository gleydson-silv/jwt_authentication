![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-Backend-green)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-API-red)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

# 📌 Projeto Django - Sistema de Autenticação e Reset de Senha

Este projeto foi desenvolvido em **Django + Django REST Framework**, com foco em **autenticação de usuários** e **fluxo de recuperação de senha via token**.  
Ele serve como base para projetos que precisam de um **backend robusto e escalável em Python**.

---

# 🛠️ Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- JWT Authentication
- PostgreSQL
- Git

---

# 🚀 Funcionalidades

### Registro de usuário
- Criação de usuário com email e senha
- Senha armazenada de forma segura (hash)

### Login
- Autenticação de usuário via email e senha
- Emissão de tokens **JWT (access e refresh)**

### Logout
- Revogação do refresh token para encerrar sessão
- Necessário enviar o **access token no header**

### Esqueceu a senha
- Envia link de reset de senha para o email do usuário
- Gera token seguro para redefinição

### Reset de senha
- Permite redefinir a senha usando o link enviado por email

### Perfil do usuário autenticado
- Endpoint protegido que retorna os dados do usuário logado
- Acesso permitido apenas com **token JWT válido**

### Custom User Model
- Modelo de usuário personalizado baseado em `AbstractUser`

---

# 🔄 Fluxo de Autenticação

### 1️⃣ Usuário se registra


POST /api/register/


### 2️⃣ Usuário faz login


POST /api/login/


### 3️⃣ API retorna tokens JWT

{
  "access": "token",
  "refresh": "token"
}
4️⃣ Usuário acessa rotas protegidas

Header necessário:

Authorization: Bearer <access_token>

5️⃣ Usuário pode acessar

GET /api/profile/

6️⃣ Caso esqueça a senha

POST /api/forgot_password/

POST /api/reset_password/<uid>/<token>/

```json

📂 Estrutura do Projeto
project/
│── manage.py
│── requirements.txt
│── .gitignore
│── README.md
│
├── project/        # Configurações principais (settings, urls, wsgi)
│
├── users/          # App de autenticação
│   ├── models.py       # CustomUser (baseado em AbstractUser)
│   ├── views.py        # Lógica dos endpoints
│   ├── serializers.py  # Serialização de dados
│   ├── urls.py         # Rotas da API de usuários
│   └── ...
│
└── ...

---


🔗 Endpoints Disponíveis
🔑 Autenticação
Método	Endpoint	Descrição
POST	/api/register/	Registrar novo usuário
POST	/api/login/	Login e retorno de token JWT
POST	/api/logout/	Logout do usuário autenticado
📥 Body exemplo — Register
{
  "email": "exemplo@email.com",
  "first_name": "Nome",
  "last_name": "Sobrenome",
  "password": "123456"
}
📥 Body exemplo — Login
{
  "email": "exemplo@gmail.com",
  "password": "123456"
}
📥 Body exemplo — Logout
{
  "refresh": "<refresh_token>"
}
👤 Perfil do Usuário
Método	Endpoint	Descrição	Autenticação
GET	/api/profile/	Retorna dados do usuário autenticado	Bearer Token
📤 Exemplo de resposta
{
  "email": "exemplo@email.com",
  "first_name": "Nome",
  "last_name": "Sobrenome"
}
🔐 Header necessário
Authorization: Bearer <access_token>
🔒 Reset de Senha
Método	Endpoint	Descrição
POST	/api/forgot_password/	Solicitar reset de senha
POST	/api/reset_password/<uid>/<token>/	Definir nova senha
📥 Body exemplo — Forgot Password
{
  "email": "exemplo@email.com"
}
📥 Body exemplo — Reset Password
{
  "password": "novasenha123"
}
⚙️ Instalação e Execução Local
🔧 Pré-requisitos

Python 3.10+

Virtualenv (recomendado)

Git

📥 Clonar o repositório
git clone https://github.com/gleydson-silv/jwt_authentication.git
cd jwt_authentication
📦 Criar e ativar ambiente virtual
Criar ambiente
python -m venv venv
Ativar no Windows
venv\Scripts\activate
Ativar no Linux / macOS
source venv/bin/activate
📚 Instalar dependências
pip install -r requirements.txt
🗄️ Rodar migrações
python manage.py makemigrations
python manage.py migrate
👤 Criar superusuário (admin)
python manage.py createsuperuser
▶️ Rodar o servidor
python manage.py runserver

A API ficará disponível em:

http://127.0.0.1:8000/
📌 Próximos Passos (Melhorias)

Configurar envio real de e-mails

SMTP

SendGrid

Amazon SES

Criar documentação automática com:

Swagger

drf-yasg

Fazer deploy da API

Heroku

Render

AWS

👨‍💻 Autor

Gleydson Luidy Batista da Silva

📧 gleydsonluidy2@gmail.com