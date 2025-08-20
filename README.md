# 🌡️ One Billion Row Challenge em Python

Este projeto explora como o Python pode encarar o **One Billion Row Challenge (1BRC)**: processar arquivos enormes (até **1 bilhão de linhas ≈ 14GB**) para calcular estatísticas de temperatura por estação meteorológica — **mínimo, média e máximo**. A ideia é comparar abordagens com foco em **tempo de execução, eficiência e simplicidade do código**.

---

## 📂 Estrutura do Repositório

- **`data/`**
  - `weather_stations.csv`: lista de estações usada na geração do dataset.
  - `measurements.txt`: arquivo massivo gerado com leituras sintéticas.

- **`src/`**
  - `create_measurements.py`: gera `measurements.txt` com milhões de linhas.
  - `using_python.py`: solução em Python puro (`csv` + `defaultdict`).
  - `using_pandas.py`: usa **pandas** para agrupar e calcular as estatísticas.
  - `using_duckdb.py`: executa SQL com **DuckDB** diretamente sobre o arquivo de texto.

- **`pyproject.toml`**
  - Configuração do projeto e dependências via **Poetry**.

---

## ⚙️ Instalação

Com o **Poetry** instalado, rode:

```bash
poetry install
```

---

## 🚀 Como Rodar

Fluxo em duas etapas:

### 1) Gerar o dataset de medições

```bash
python src/create_measurements.py
```

- Gera `data/measurements.txt` (por padrão, **100 milhões de linhas**).
- Exibe o **tempo total de geração**.

### 2) Processar os dados

Escolha uma das abordagens para calcular **min/média/max** por estação:

**Python puro**
```bash
python src/using_python.py
```

**Pandas**
```bash
python src/using_pandas.py
```

**DuckDB**
```bash
python src/using_duckdb.py
```

Cada script imprime:
- **Tempo total de processamento**
- Estatísticas por estação (**min**, **avg**, **max**)

---

## 🎯 Objetivo

Mais do que “passar no desafio”, este repositório é um **estudo comparativo** de estratégias de processamento de grandes volumes de dados em Python, evidenciando os **trade-offs** entre:
- Implementação direta (Python puro)
- Produtividade e conveniência (pandas)
- Consultas SQL em arquivo texto (DuckDB)
