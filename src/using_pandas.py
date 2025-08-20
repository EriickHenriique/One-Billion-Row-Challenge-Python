import pandas as pd
import time
from pathlib import Path

PATH_DO_TXT = 'data\measurements.txt'

def processar_temperaturas(path_do_txt: Path):

    print('Iniciando o processamento dos dados')
    inicio = time.time()
    df = pd.read_csv("data/measurements.txt", sep=";", header = None, names=['Estacao','Temperatura'])

    print('Agrupando Itens..')
    estacao_group = df.groupby('Estacao')    
    resumo = estacao_group['Temperatura'].agg(['min', 'max', 'mean'])
    
    fim = time.time()
    print(f'Processamento concluido em {fim - inicio:.2f} segundos') 
    return resumo


if __name__ == '__main__':
    path_do_text: Path = PATH_DO_TXT
    resultados = processar_temperaturas(path_do_text)










    




