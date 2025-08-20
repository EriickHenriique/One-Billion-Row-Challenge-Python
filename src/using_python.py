from csv import reader
from collections import defaultdict
import time


from pathlib import Path

PATH_DO_TXT = 'data\measurements.txt'

def processar_temperaturas(path_do_txt: Path):

    print('Iniciando o processamento dos dados')
    inicio = time.time()

    temperatura_por_estacao = defaultdict(list)

    with open(file=path_do_txt, mode='r', encoding='utf-8') as file:
        _reader = reader(file, delimiter=';')
        for row in _reader:
            nome_da_estacao, temperatura = str(row[0]), float(row[1])
            temperatura_por_estacao[nome_da_estacao].append(temperatura)    

    print('Dados carregados com sucesso')
        
    resultado = {}

    for nome_da_estacao, temperatura in temperatura_por_estacao.items():
        temp_min = min(temperatura)
        temp_max = max(temperatura)
        temp_mean = sum(temperatura) / len(temperatura)
        resultado[nome_da_estacao] = (temp_min, temp_max, temp_mean)
    
    print('Estatisticas calculadas. Ordenando..')
    sorted_results = dict(sorted(resultado.items()))

    fim = time.time()

    formatted_results = {nome_da_estacao: f"{temp_min:.1f}/{temp_mean:.1f}/{temp_max:.1f}" for nome_da_estacao, (temp_min, temp_mean, temp_max) in sorted_results.items()}

    print(f'Processamento concluido em {fim - inicio:.2f} segundos') 

    return formatted_results



if __name__ == '__main__':
    path_do_text: Path = PATH_DO_TXT
    resultados = processar_temperaturas(path_do_text)











