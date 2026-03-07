![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-Backend-green)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-API-red)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

# 📌 Projeto Django - Sistema de Autenticação e Reset de Senha

Este repositório contém uma API construída com **Django** e **Django REST Framework**. O foco principal é fornecer um *backend* seguro para autenticação de usuários, utilizando **JWT** e com suporte a recuperação de senha via e-mail.

O projeto pode servir como base para aplicações que precisem de uma estrutura de login/recuperação robusta e facilmente customizável.

---

## 🛠️ Tecnologias utilizadas

- Python 3.10+
- Django
- Django REST Framework
- JWT (djangorestframework-simplejwt)
- PostgreSQL (ou SQLite para desenvolvimento)
- Git

---

## 🚀 Funcionalidades principais

- **Registro** de usuário com e-mail e senha
- **Login** retornando tokens JWT (*access* e *refresh*)
- **Logout** com invalidação do token de refresh
- **Recuperação de senha** via link enviado por e-mail
- **Reset de senha** utilizando token seguro
- **Perfil do usuário** (rota protegida por JWT)
- **Custom User Model** estendendo `AbstractUser`

---

## 🔄 Fluxo de autenticação

1. Usuário se registra
   ```http
   POST /api/register/
   ```
2. Faz login
   ```http
   POST /api/login/
   ```
3. Recebe tokens JWT:
   ```json
   {
     "access": "<token>",
     "refresh": "<token>"
   }
   ```
4. Acessa rotas protegidas enviando o header `Authorization: Bearer <access_token>`
5. Exemplo de rota protegida:
   ```http
   GET /api/profile/
   ```
6. Caso esqueça a senha:
   ```http
   POST /api/forgot_password/
   ```
   e em seguida
   ```http
   POST /api/reset_password/<uid>/<token>/
   ```

---

## 📂 Estrutura do projeto (simplificada)

```
manage.py
requirements.txt
README.md

backend/           # configurações Django (settings, urls, wsgi, asgi)
users/             # app de autenticação
  ├── models.py        # CustomUser
  ├── serializers.py   # serializers
  ├── views.py         # lógica de API
  ├── urls.py          # rotas do app
  └── ...
```

---

## 🔗 Endpoints disponíveis

### 🔑 Autenticação

| Método | Endpoint               | Descrição                       |
|--------|------------------------|---------------------------------|
| POST   | `/api/register/`       | Registrar novo usuário          |
| POST   | `/api/login/`          | Login e retorno de tokens JWT   |
| POST   | `/api/logout/`         | Logout (invalida refresh token) |

**Exemplo de body**
```json
{
  "email": "exemplo@email.com",
  "first_name": "Nome",
  "last_name": "Sobrenome",
  "password": "123456"
}
```

### 👤 Perfil do usuário

| Método | Endpoint               | Descrição                           | Autenticação     |
|--------|------------------------|-------------------------------------|------------------|
| GET    | `/api/profile/`        | Dados do usuário autenticado        | Bearer Token     |
|--------|------------------------|-------------------------------------|------------------|
| PUT    | `/api/profile/update/` |Atualiza Dados do usuário autenticado| Bearer Token     |

**Resposta de exemplo**
```json
{
  "email": "exemplo@email.com",
  "first_name": "Nome",
  "last_name": "Sobrenome"
}

**Resposta de exemplo**
```json
{
  "email": "exemplo@email.com",
  "first_name": "Nome",
  "last_name": "Sobrenome"
}

```

### 🔒 Reset de senha

| Método | Endpoint                               | Descrição               |
|--------|----------------------------------------|-------------------------|
| POST   | `/api/forgot_password/`                | Solicitar link por e-mail |
| POST   | `/api/reset_password/<uid>/<token>/`   | Definir nova senha        |

**Body exemplos**
```json
{ "email": "exemplo@email.com" }
```

```json
{ "password": "novasenha123" }
```

---

## ⚙️ Instalação e execução local

### Pré-requisitos

- Python 3.10 ou superior
- Virtualenv (recomendado)
- Git

### Passos

```bash
git clone https://github.com/gleydson-silv/jwt_authentication.git
cd jwt_authentication
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate       # Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

A API ficará acessível em `http://127.0.0.1:8000/`.

---

## 📌 Próximos passos / melhorias

- Configurar envio real de e-mails (SMTP, SendGrid, Amazon SES)
- Adicionar testes automatizados para cobertura
- Suporte a OAuth2/social login

---

© 2026 - Licença MIT


👨‍💻 Autor

Gleydson Luidy Batista da Silva

📧 gleydsonluidy2@gmail.com