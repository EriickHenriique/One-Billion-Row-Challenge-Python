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
def conversão_bytes(num):
    for x in ['bytes','KiB','MiB','GiB']:
        if num < 1024:
            return "%3.1f %s" % (num, x)
        num /= 1024.0



        


        







