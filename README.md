# 📌 Desafio Técnico - Planos de Sáude - ANS

## 📖 Sobre o Projeto
Este projeto implementa soluções de **Web Scraping, Transformação de Dados, Banco de Dados e API**. A aplicação é dividida em módulos independentes, cada um utilizando tecnologias adequadas para melhor desempenho e organização.

## 🏗 Estrutura do Projeto
```
├── web_scraping/          # Código para download e compactação dos anexos
├── data_transformation/   # Extração, transformação e salvamento dos dados
├── database/              # Scripts SQL para estruturação e análise de dados
       ├── queries         #Consultas sql
├── data/                  # Dados extraídos e transformados
├── api/                   # Backend FastAPI para consultas via API
├── frontend/              # Aplicação Vue.js para interface gráfica
├──evidencias              #evidências do funcionamento de cada modulo
├── main.py
├── main_contability.py 
└── README.md              # Documentação
```

## 🚀 Tecnologias Utilizadas
### 🔹 Web Scraping
- **Python**: `requests`, `BeautifulSoup`, `Pdfplumber`

### 🔹 Transformação de Dados
- **Python**:  `pandas`, `ZipFile`

### 🔹 Banco de Dados
-  **PostgreSQL 10+**
- Ferramentas: `psycopg2`

### 🔹 API
- **FastAPI** (Python)
- **Vue.js** (Frontend)

## 🔧 Configuração e Instalação
### 📥 Clonando o Repositório
```bash
git clone https://github.com/leh826/web-scraping-analytics.git
```
### 🐍 Configurar o Ambiente Python
#### 🔹Criar o ambiente virtual

```bash
python -m venv .venv
```
#### 🔹Ativar o ambiente virtual
- Linux/Mac:

```bash
source venv/bin/activate
```
- Windows:

```bash
.venv\Scripts\activate
```
### 📌 Instalando Dependências
#### 🔹 Python (Web Scraping, Transformação e API)
```bash
pip install -r requirements.txt
```
#### 🔹 Vue.js (Frontend)
```bash
cd frontend
npm install
```

### Execução de Scripts 
## Teste 1
Na pasta `WebScraping` execute o arquivo scraping-attachement para que seja baixado os anexo.

## Teste 2
Na pasta data-transformtion execute o arquivo extract-data, para extrair os dados do anexo 1.

## Teste 3
1. Na pasta `WebScraping` execute o arquivo scraping-contabilidade para que seja baixado os arquivos.
2. Execute o main_contability para que seja criada a tabela dados_financeiros e agrupado os arquivos csv.
3. Execute o main para ser criado a tabela ans_operados, tranformado os dados e inseridos.

##  Configuração do Banco de Dados
### 🔹Requisitos Mínimos
 Certifique-se de que sua máquina atenda aos seguintes requisitos:
- Docker instalado (versão mais recente preferível).

### 🔹Crie um Arquivo `.env`
Crie um arquivo `.env` na raiz do projeto contendo as seguintes variáveis:

```env
DB_HOST= seu host
DB_PORT=5432
DB_NAME= ans_operadoras
DB_USER=seu_usuario
DB_PASSWORD=sua_senha

PGADMIN_DEFAULT_EMAIL= email_de_acesso
PGADMIN_DEFAULT_PASSWORD=senha_de_acesso
```
### 🔹Rode o docker compose
```bash
docker-compose up -d
```
### 🔹Acesse o pgAdmin
Pela URL `https://localhost:5050` você pode acessar o pgAdmin, no seu login:
- Insira seu email_de_acesso
- Insira sua senha_de_acesso

### 🔹Importação de arquivos
Dentro do PgAdmin exporte o arquivo csv `adjusted_data.csv` na tabela `dados_financeiros` gerado nas execuções dos scripts.

## Execução do Projeto

### 🔹 Executando a API
```bash
cd api
uvicorn main:app --reload
```

### 🔹 Executando o Frontend
```bash
cd frontend
npm run dev
```

## 📊 Consultas no Banco de Dados
1. Na pasta `/database/queries` possuem consultas para serem executadas no PGAdmin.
2. Na pasta `evidência` contém prints de comprovação do funcionamento do projeto.

## 🚀 Diferenciais Implementados
✅ Arquitetura modular e bem estruturada
✅ Controle de versão com Git
✅ Infraestrutura conternizada 

---
📌 **Desenvolvido por [Letícia Souza]** 📌 Desafio Técnico 
#
