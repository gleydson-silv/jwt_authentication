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
- django-allauth (login social)
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
- **Login social com Google** via django-allauth

---

## 🔄 Fluxo de autenticação

1. Usuário se registra
   ```http
   POST /register/
   ```
2. Faz login
   ```http
   POST /login/
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
   GET /profile/
   ```
6. Caso esqueça a senha:
   ```http
   POST /forgot_password/
   ```
   e em seguida
   ```http
   POST /reset_password/<uid>/<token>/
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
| POST   | `/register/`       | Registrar novo usuário          |
| POST   | `/login/`          | Login de usuário                |
| POST   | `/logout/`         | Logout (invalida refresh token) |

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

| Método | Endpoint               | Descrição                             | Autenticação     |
|--------|------------------------|---------------------------------------|------------------|
| GET    | `/profile/`        | Dados do usuário autenticado          | Bearer Token     |
| PUT    | `/profile/update/` | Atualiza Dados do usuário autenticado | Bearer Token     |
| PATCH  | `/profile/update/partial/` | Atualiza parcialmente dados do usuário autenticado | Bearer Token     |

**Resposta de exemplo**
```json
{
  "email": "exemplo@email.com",
  "first_name": "Nome",
  "last_name": "Sobrenome"
}
```

**Resposta de exemplo**
```json
{
  "email": "exemplo@email.com",
  "first_name": "Nome",
  "last_name": "Sobrenome"
}

```

### 🔒 Reset de senha

| Método | Endpoint                               | Descrição                 |
|--------|----------------------------------------|---------------------------|
| POST   | `/forgot_password/`                | Solicitar link por e-mail |
| POST   | `/reset_password/<uid>/<token>/`   | Definir nova senha        |

### 🔐 Troca de senha 

| Método | Endpoint               | Descrição                                         | Autenticação     |
|--------|------------------------|---------------------------------------------------|------------------|
| POST   | `/change_password/`| Altera a senha do usuário autenticado             | Bearer Token     |

### 🗑️ Conta do usuário

| Método | Endpoint               | Descrição                           | Autenticação     |
|--------|------------------------|-------------------------------------|------------------|
| DELETE | `/account/delete/` | Deleta a conta do usuário atual     | Bearer Token     |

### 🔍 Verificação de Token

| Método | Endpoint             | Descrição                                           |
|--------|----------------------|-----------------------------------------------------|
| POST   | `/token/verify/` | Verifica se um token JWT de refresh/access é válido |

### 🔐 Autenticação em Dois Fatores (2FA)

| Método | Endpoint                 | Descrição                                          | Autenticação     |
|--------|--------------------------|----------------------------------------------------|------------------|
| POST   | `/2fa/verify/`       | Valida o código TOTP e emite tokens JWT            | -                |
| POST   | `/2fa/enable/`       | Gera segredo e ativa 2FA para o usuário            | Bearer Token     |
| POST   | `/2fa/disable/`      | Desativa 2FA no usuário                            | Bearer Token     |

### 🌐 Login social (Google)

| Método | Endpoint                      | Descrição                          |
|--------|-------------------------------|------------------------------------|
| GET    | `/accounts/google/login/`     | Inicia o login com Google          |

Após autenticar, o allauth faz redirect conforme `LOGIN_REDIRECT_URL` em `backend/settings.py`.

---

## 🎨 Front-end (UI)

O projeto agora inclui um front-end moderno e responsivo para testar todas as rotas diretamente no navegador.

### Rotas da UI

- `/app/` (home)
- `/app/register/`
- `/app/login/`
- `/app/logout/`
- `/app/forgot-password/`
- `/app/reset-password/`
- `/app/reset-password/<uidb64>/<token>/`
- `/app/change-password/`
- `/app/profile/`
- `/app/profile/update/`
- `/app/profile/update/partial/`
- `/app/token/verify/`
- `/app/token/refresh/`
- `/app/account/delete/`
- `/app/2fa/verify/`
- `/app/2fa/enable/`
- `/app/2fa/disable/`
- `/app/security/`

### Login com Google

O botão de login com Google aponta para a rota do allauth:

- `/accounts/google/login/`

### Observações

- As respostas exibidas na UI são mensagens curtas, sem JSON.
- Em caso de sucesso, a interface redireciona para o próximo passo do fluxo.






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

## 🐳 Execução com Docker

1. Copie o arquivo `.env.example` para `.env` e ajuste se necessário
2. Suba os containers

```bash
docker compose up --build
```

3. Em outro terminal, rode as migrations e crie o superuser

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
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
