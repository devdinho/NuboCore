
# ⚙️ NuboCore

**NuboCore** é o backend principal do ecossistema **Nubo**, desenvolvido com **Django**, responsável por gerenciar recursos dinâmicos (feature flags, ambientes, configurações)

NuboCore pode ser utilizado via API por outras interfaces ou serviços.

---

## 🚀 Tecnologias Utilizadas

- [Python 3.11+](https://www.python.org/)
- [Django 5](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [JWT](https://django-rest-framework-simplejwt.readthedocs.io/) (autenticação segura)

---

## 📦 Instalação

### 1. Clone o projeto

```bash
git clone https://github.com/devdinho/nubocore.git
cd nubocore
````

### 2. Copie e cole o arquivo .env.example e renomeie para .env

### 3. Modifique para suas varáveis de ambiente

### 4. Execute o container docker

```bash
docker compose up --build
```

---

## 🧪 Endpoints REST (exemplo)

* `POST /api/token/` – autenticação JWT
* `GET /api/resources/` – lista de recursos configuráveis
* `GET /api/observability/system/` – dados de CPU, RAM, disco
* `GET /api/containers/` – listagem de containers Docker
* `POST /api/deploy/` – aciona um deploy com parâmetros definidos

---
##### Documentação MkDocs: `/api/docs/`
---


## 📁 Estrutura Inicial

```
nubocore/
├── core/               # app principal (recursos, observabilidade)
├── terminal/           # gerenciamento de sessões de terminal remoto
├── docker_monitor/     # integração com containers Docker
├── deploy/             # orquestração de pipelines
├── users/              # login, JWT, permissões
├── static/
├── media/
├── manage.py
├── requirements.txt
└── nubocore/settings.py
```

---

## ⚙️ Variáveis de Ambiente

Crie um `.env`:

```env
SECRET_KEY=chave-secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=admin123
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://localhost:6379
```

---

## 🔐 Autenticação

Usa JWT com [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/).
Endpoints disponíveis:

* `POST /api/token/` – login
* `POST /api/token/refresh/` – refresh
* `GET /api/me/` – dados do usuário logado

---

## ✨ Roadmap

* [x] Setup de projeto com Django e DRF
* [x] Autenticação via JWT
* [x] API de recursos dinâmicos (feature flags, ambientes)
* [ ] Sistema de permissões com papéis

---

## 🔗 Relacionamento com o Nubo Panel

O **Nubo Panel** (frontend) consome o **NuboCore** via REST e WebSocket, para:

* Listar e editar recursos

---

## 👤 Autor

Anderson Freitas
[GitHub](https://github.com/devdinho)
[LinkedIn](https://linkedin.com/in/freitas-anderson)

---

## 📄 Licença

MIT