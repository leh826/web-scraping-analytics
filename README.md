# 📌 Desafio Técnico - Planos de Sáude - ANS

## 📖 Sobre o Projeto
Este projeto implementa soluções de **Web Scraping, Transformação de Dados, Banco de Dados e API**. A aplicação é dividida em módulos independentes, cada um utilizando tecnologias adequadas para melhor desempenho e organização.

## 🏗 Estrutura do Projeto
```
├── web_scraping/          # Código para download e compactação dos anexos
├── data_transformation/   # Extração, transformação e salvamento dos dados
├── database/              # Scripts SQL para estruturação e análise de dados
├── data/                  # Dados extraídos e transformados
├── api/                   # Backend FastAPI para consultas via API
├── frontend/              # Aplicação Vue.js para interface gráfica
├── tests/                 # Testes automatizados
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

##  Configuração do Banco de Dados
### 🔹Requisitos Mínimos
 Certifique-se de que sua máquina atenda aos seguintes requisitos:
- Docker instalado (versão mais recente preferível).
- Docker Compose instalado.
- Espaço em disco suficiente para armazenar os dados do banco de dados e arquivos CSV.

### 🔹Crie um Arquivo `.env`
Crie um arquivo `.env` na raiz do projeto contendo as seguintes variáveis:

```env
DB_HOST= seu host
DB_PORT=5432
DB_NAME= ans_operadoras
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```
### Rode o docker compose
```bash
docker-compose up -d
```
### Acesse o pgAdmin
Pela URL `https://localhost:5050` você pode acessar o pgAdmin e visualizar o banco de dados

### Importação de arquivos
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
- **Maiores despesas no último trimestre**:
```sql
SELECT operadora, SUM(valor) AS total
FROM despesas
WHERE categoria = 'ASSISTÊNCIA MÉDICO-HOSPITALAR'
AND data BETWEEN CURRENT_DATE - INTERVAL '3 months' AND CURRENT_DATE
GROUP BY operadora
ORDER BY total DESC
LIMIT 10;
```
- **Maiores despesas no último ano**:
```sql
SELECT operadora, SUM(valor) AS total
FROM despesas
WHERE categoria = 'ASSISTÊNCIA MÉDICO-HOSPITALAR'
AND data BETWEEN CURRENT_DATE - INTERVAL '1 year' AND CURRENT_DATE
GROUP BY operadora
ORDER BY total DESC
LIMIT 10;
```

## 📌 Testes
### 🔹 Testes de Unidade e Integração
Para rodar os testes:
```bash
pytest tests/
```

## 🚀 Diferenciais Implementados
✅ Testes automatizados
✅ Melhorias de performance (uso de indexação SQL e processamento assíncrono)
✅ Arquitetura modular e bem estruturada
✅ Controle de versão com Git
✅ Infraestrutura conternizada 

## 📄 Licença
Este projeto é privado e de uso restrito.

---
📌 **Desenvolvido por [Letícia Souza]** 📌 Desafio Técnico 