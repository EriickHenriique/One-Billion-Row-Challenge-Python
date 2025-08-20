import os
import time
import random
import sys
from datetime import timedelta


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


def tamanho_arquivo_estimado(estacoes, linhas_a_criar):
    """
    Tries to estimate how large a file the test data will be
    """
    max_string = float('-inf')
    min_string = float('inf')
    per_record_size = 0
    record_size_unit = "bytes"

    for estacao in estacoes:
        if len(estacao) > max_string:
            max_string = len(estacao)
        if len(estacao) < min_string:
            min_string = len(estacao)
        per_record_size = ((max_string + min_string * 2) + len(",-123.4")) / 2

    tamanho_arquivo = linhas_a_criar * per_record_size
    human_file_size = conversao_bytes(tamanho_arquivo)

    return f"O tamanho estimado do arquivo é:  {human_file_size}.\nO tamanho final será provavelmente muito menor (metade)."







        


        







