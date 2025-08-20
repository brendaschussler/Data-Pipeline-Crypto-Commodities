# 📊 Data Pipeline – Crypto & Commodities  

Este projeto implementa um **pipeline de dados** em Python que coleta periodicamente cotações do **Bitcoin** e de **commodities** (ouro, petróleo e prata) e as armazena em um **banco de dados PostgreSQL**.  

O objetivo é demonstrar práticas fundamentais de **engenharia de dados** como **ingestão**, **transformação**, **armazenamento estruturado** e **automação** de fluxos de coleta.  

---

## 🚀 Visão Geral do Pipeline  

O fluxo segue a lógica **ETL (Extract, Transform, Load)**:  

1. **Extract (Extração)**  
   - Coleta do preço **spot** do Bitcoin via API da Coinbase.  
   - Coleta de commodities (`GC=F` ouro, `CL=F` petróleo, `SI=F` prata) via `yfinance`.  

2. **Transform (Transformação)**  
   - Padronização das informações em um **DataFrame Pandas**.  
   - Normalização das colunas: `ativo`, `preco`, `moeda`, `horario_coleta`.  

3. **Load (Carregamento)**  
   - Inserção dos dados na tabela `cotacoes` em um banco **PostgreSQL**.  
   - Processo executado automaticamente a cada **60 segundos** (batch em mini-lotes).
  
## ⚙️ Configuração  

### 1. Clone o repositório  

```bash
git clone https://github.com/brendaschussler/Data-Pipeline-Crypto-Commodities.git
cd Data-Pipeline-Crypto-Commodities
```

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
### 3. Instale as dependências
```bash
pip install -r requirements.txt
```
### 4. Configure o arquivo .env
```bash
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
```
### 5. Configure o PostgreSQL
```bash
CREATE TABLE IF NOT EXISTS bronze_cotacoes (
  id              BIGSERIAL PRIMARY KEY,
  ativo           TEXT NOT NULL,           
  preco           NUMERIC(18,6) NOT NULL,  
  moeda           CHAR(3) NOT NULL DEFAULT 'USD',
  horario_coleta  TIMESTAMPTZ NOT NULL,    
  inserido_em     TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### ▶️ Execução do Pipeline
```bash
python get_prices_loop_db.py
```

A cada 60 segundos, novos registros são ingeridos no banco de dados.
