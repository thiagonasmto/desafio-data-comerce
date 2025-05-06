# 📊 Dashboard de Comércio Exterior

Este repositório contém duas soluções para visualização de dados de comércio exterior com base em arquivos CSV:

---

## 🧭 Estrutura do Repositório

### 1. `dashboard_streamlit/` ✅

Aplicação completa utilizando **Streamlit**. Ideal para testes rápidos e análise exploratória.

- Já está **totalmente funcional**.
- Permite upload de arquivos CSV e visualização de gráficos interativos.
- Pode ser executada com o comando padrão:

```bash
streamlit run app.py
````

---

### 2. `dashboard_web/` 🛠️

Aplicação **fullstack em desenvolvimento** com foco em escalabilidade e interface moderna:

* **Back-end**: Django + Django REST Framework
* **Front-end**: React + TypeScript
* **Banco de dados**: PostgreSQL

📌 **Status atual:**

* O upload de arquivos já funciona via API.
* Os gráficos estão sendo gerados em arquivos HTML.
* Ainda falta a integração desses gráficos à interface principal do front-end.

---

## 🚀 Tecnologias

* [Django 5.2](https://docs.djangoproject.com/en/5.2/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [React](https://react.dev/) + [TypeScript](https://www.typescriptlang.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [CORS Headers](https://pypi.org/project/django-cors-headers/)
* [Streamlit](https://streamlit.io/)

---

## 📁 Estrutura da Pasta `dashboard_web`

```
dashboard_web/
├── backend/              # Projeto Django
├── frontend/             # Projeto React + TypeScript
├── data/                 # CSVs e dados brutos
├── venv/                 # Ambiente virtual Python
├── manage.py             # Comando de gerenciamento do Django
├── get_data_bd.py        # Scripts auxiliares
├── load_csv.py
├── top_exp_per_month.py
├── top_exp_vizualizer.py
├── top_imp_vizualizer.py
```

---

## ⚙️ Como rodar a versão web (Django + React)

### 🔧 Pré-requisitos

* Python 3.11+
* Node.js 18+
* PostgreSQL (porta 5433)
* Git

### 🐍 Configurando o back-end (Django)

1. Crie e ative o ambiente virtual:

```bash
cd dashboard_web
python -m venv venv
venv\Scripts\activate
```

2. Instale as dependências:

```bash
pip install django djangorestframework psycopg2-binary django-cors-headers
```

3. Configure o banco de dados PostgreSQL:

Crie o banco e usuário no seu PostgreSQL com os seguintes dados (ou edite em `backend/settings.py`):

```sql
CREATE DATABASE seu_bone_db;
CREATE USER seu_bone_user WITH PASSWORD 'seubone123';
ALTER ROLE seu_bone_user SET client_encoding TO 'utf8';
ALTER ROLE seu_bone_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE seu_bone_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE seu_bone_db TO seu_bone_user;
```

4. Rode as migrações e inicie o servidor:

```bash
python manage.py migrate
python manage.py runserver
```

---

### 🌐 Configurando o front-end (React + TypeScript)

1. Acesse a pasta do front-end:

```bash
cd frontend
```

2. Instale as dependências:

```bash
npm install
```

3. Inicie o servidor de desenvolvimento:

```bash
npm run dev
```

Se você usa Vite ou Create React App, ajuste o comando acima para `npm start` ou `vite`.

4. (Opcional) Configure proxy para API:

Adicione ao `package.json`:

```json
"proxy": "http://localhost:8000"
```

---

## 🔄 Comunicação entre Front e Back

* O backend roda por padrão em `http://localhost:8000`.
* O frontend roda em `http://localhost:5173` (ou 3000).
* CORS já está habilitado para todas as origens (`CORS_ALLOW_ALL_ORIGINS = True`).

---

## 📦 Scripts úteis (`dashboard_web`)

* `get_data_bd.py`, `load_csv.py`: scripts para carga e leitura de dados do banco.
* `top_exp_vizualizer.py`: visualização dos top exportadores.
* `top_exp_per_month.py`: visualização mês a mês.
* `top_imp_vizualizer.py`: visualização dos top importadores.

---

## 📝 Endpoints disponíveis (Django)

| Método | URL                  | Descrição              |
| ------ | -------------------- | ---------------------- |
| GET    | `/`                  | Página inicial         |
| POST   | `/upload-csv/`       | Upload de arquivos CSV |
| GET    | `/top-3-exportados/` | Retorna top 3 produtos |

---

## 📌 Contribuindo

Sinta-se livre para abrir *issues* ou *pull requests* para melhorias nas duas versões do projeto.
A versão Streamlit serve como protótipo funcional e inspiração para o desenvolvimento completo da aplicação web.

---

```

Se quiser, posso gerar esse arquivo e te enviar pronto para salvar no repositório. Deseja isso?
```
