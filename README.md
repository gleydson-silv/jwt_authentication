# 📌 Projeto Django - Sistema de Autenticação e Reset de Senha

Este projeto foi desenvolvido em **Django + Django REST Framework**, com foco em **autenticação de usuários** e **fluxo de recuperação de senha via token**.  
Ele serve como base para projetos que precisam de um backend robusto e escalável em Python.

---

## 🚀 Funcionalidades

-Registro de usuário:
Criação de usuário com email e senha.
Senha armazenada de forma segura (hash bcrypt).

-Login:
Autenticação de usuário via email e senha.
Emissão de tokens JWT (access e refresh).

-Logout:
Revogação do refresh token para encerrar sessão.
Necessita enviar o access token no header.

-Esqueceu a senha:
Envia link de reset de senha para o email do usuário.
Gera token seguro para resetar senha.

-Reset de senha:
Permite redefinir a senha usando o link enviado por email.

-Suporte a custom user model baseado em `AbstractUser`

---

## 📂 Estrutura do Projeto
project/
│── manage.py
│── requirements.txt
│── .gitignore
│── README.md
│
├── project/ # Configurações principais (settings, urls, wsgi)
│
├── users/ # App de autenticação
│ ├── models.py # CustomUser (baseado em AbstractUser)
│ ├── views.py # Lógica dos endpoints
│ ├── serializers.py # Serialização de dados
│ ├── urls.py # Rotas da API de usuários
│ └── ...
│
└── ...


---

## 🔗 Endpoints Disponíveis

### 🔑 Autenticação

| Método | Endpoint                  | Descrição                     | Body Exemplo |
|--------|---------------------------|--------------------------------|--------------|
| POST   | `/api/register/`          | Registrar novo usuário         | `{ "email": "exemplo@email.com","password": "123456"` |
| POST   | `/api/login/`             | Login e retorno de token JWT   | `{ "email": "exemplo@gmail.com","password": "123456"` |
| POST   | `/api/logout/`            | Logout do usuário autenticado  |  Header: Authorization: Bearer <access>
Body: {"refresh": "<refresh_token>"} |

### 🔒 Reset de Senha

| Método | Endpoint                                           | Descrição                                      | Body Exemplo |
|--------|----------------------------------------------------|------------------------------------------------|--------------|
| POST   | `/api/request_reset_password/`                     | Solicitar reset de senha (envia e-mail com link) | `{ "email": "exemplo@email.com" }` |
| POST   | `/api/reset_password/<uid>/<token>/`               | Definir nova senha usando o link recebido       | `{ "password": "novasenha123" }` |

---

## ⚙️ Instalação e Execução Local

### 🔧 Pré-requisitos

- Python 3.10+  
- Virtualenv (recomendado)  
- Git  

### 📥 Clonar o repositório

```bash
git clone https://github.com/gleydson-silv/jwt_authentication.git
cd seu-projeto

📦 Criar e ativar ambiente virtual
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Linux/macOS
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


📌 Próximos Passos (Sugestões de Melhorias)

Configurar envio real de e-mails (SMTP / SendGrid / Amazon SES)

Implementar autenticação JWT com djangorestframework-simplejwt

Criar documentação automática com drf-yasg ou Swagger

Deploy em Heroku / Render / AWS EC2

👨‍💻 Autor
Desenvolvido por Gleydson Luidy Batista da Silva 💻
📧 gleydsonluidy2@gmail.com

