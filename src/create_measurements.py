import os
import time
import random
import sys


#Separa o nome das Cidades
def NomeEstacoes():
    nome_estacoes = []
    with open(file='./data/weather_stations.csv',mode='r',encoding='utf-8') as arquivo:
        conteudo_arquivo = arquivo.read().splitlines()
        for estacoes in conteudo_arquivo:
            if '#' in estacoes:
                next
            else:
                nome_estacoes.append(estacoes.split(';')[0])
    return nome_estacoes

#Converte os valores
def conversao_bytes(num):
    for x in ['bytes','KiB','MiB','GiB']:
        if num < 1024:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


# Formata os segundos para a formatação de tempo correta.
def tempo_formatado(segundos):
    if segundos < 60:
        return f"{segundos:.3f} segundos"
    elif segundos < 3600:
        minutos, segundos = divmod(segundos, 60)
        return f"{int(minutos)} minutos {int(segundos)} segundos"
    else:
        horas, resto = divmod(segundos, 3600)
        minutos, segundos = divmod(resto, 60)
        if minutos == 0:
            return f"{int(horas)} horas {int(segundos)} segundos"
        else:
            return f"{int(horas)} horas {int(minutos)} minutos {int(segundos)} segundos"


# Estima o tamanho do arquivo
def tamanho_arquivo_estimado(estacoes, linhas_a_criar):

    max_string = float('-inf')
    min_string = float('inf')
    tamanho = 0

    for estacao in estacoes:
        if len(estacao) > max_string:
            max_string = len(estacao)
        if len(estacao) < min_string:
            min_string = len(estacao)
        tamanho = ((max_string + min_string * 2) + len(",-123.4")) / 2

    tamanho_arquivo = linhas_a_criar * tamanho
    human_file_size = conversao_bytes(tamanho_arquivo)

    return f"O tamanho estimado do arquivo é:  {human_file_size}.\nO tamanho final será provavelmente muito menor (metade)."


# Gera e Preenche o arquivo com o tamanho de linhas pré-definidas
def contrucao_arquivo(estacoes, linhas_a_criar):

    inicio = time.time()
    temp_frio = -99.9
    temp_quente = 99.9
    nomes_estacoes = random.choices(estacoes, k=10_000)
    linhas_tamanho = 10000 
    print('Criando o arquivo... isso vai demorar uns 10 minutos...')

    try:
        with open("./data/measurements.txt", 'w', encoding="utf-8") as file:
            for s in range(0,linhas_a_criar // linhas_tamanho):
                
                batch = random.choices(nomes_estacoes, k=linhas_tamanho)
                prepped_deviated_batch = '\n'.join([f"{estacao};{random.uniform(temp_frio, temp_quente):.1f}" for estacao in batch]) 
                file.write(prepped_deviated_batch + '\n')
                
        sys.stdout.write('\n')
    except Exception as e:
        print("Something went wrong. Printing error info and exiting...")
        print(e)
        exit()
    
    fim = time.time()
    tempo_total = fim - inicio
    tamanho_do_arquivo = os.path.getsize("./data/measurements.txt")
    human_file_size = conversao_bytes(tamanho_do_arquivo)
 
    print("Arquivo escrito com sucesso data/measurements.txt")
    print(f"Tamanho final:  {human_file_size}")
    print(f"Tempo decorrido: {tempo_formatado(tempo_total)}")

def main():
    linhas_a_criar = 100_000_000
    estacoes = []
    estacoes = NomeEstacoes()
    print(tamanho_arquivo_estimado(estacoes, linhas_a_criar))
    contrucao_arquivo(estacoes, linhas_a_criar)
    print("Arquivo de teste finalizado.")


if __name__ == "__main__":
    main()
exit()






        


        







