     1  # One-Billion-Row-Challenge-Python
     2
     3  Este repositório demonstra diferentes abordagens para o desafio **One Billion Row Challenge** utilizando Python. O objet
ivo é processar de forma eficiente um arquivo massivo contendo até 1 bilhão de linhas (~14GB) e calcular estatísticas como mínim
o, máximo e média de temperatura por estação meteorológica.
     4
     5  ## Estrutura do projeto
     6
     7  - **data/**
     8    - `weather_stations.csv`: lista de estações meteorológicas usadas para gerar o dataset de medições.
     9  - **src/**
    10    - `create_measurements.py`: gera o arquivo `measurements.txt` com milhões de leituras sintéticas de temperatura.
    11    - `using_python.py`: implementa o processamento em Python puro utilizando `csv` e `defaultdict`.
    12    - `using_pandas.py`: usa a biblioteca **pandas** para agrupar e calcular as estatísticas de cada estação.
    13    - `using_duckdb.py`: executa uma consulta SQL com **DuckDB** diretamente sobre o arquivo de texto.
    14  - `pyproject.toml`: configuração do projeto e dependências gerenciadas com **Poetry**.
    15
    16  ## Instalação
    17
    18  Com o Poetry instalado, instale as dependências:
    19
    20  ```bash
    21  poetry install
    22  ```
    23
    24  ## Como usar
    25
    26  1. **Gerar o arquivo de medições**
    27
    28     ```bash
    29     python src/create_measurements.py
    30     ```
    31
    32     O script cria `data/measurements.txt` (100 milhões de linhas por padrão) e informa o tempo gasto.
    33
    34  2. **Processar os dados**
    35
    36     Escolha uma das abordagens abaixo para calcular `min/média/max` por estação:
    37
    38     - Python puro:
    39       ```bash
    40       python src/using_python.py
    41       ```
    42     - Pandas:
    43       ```bash
    44       python src/using_pandas.py
    45       ```
    46     - DuckDB:
    47       ```bash
    48       python src/using_duckdb.py
    49       ```
    50
    51  Cada script exibe o tempo total de processamento e as estatísticas calculadas.
