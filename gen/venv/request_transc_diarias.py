# Importação das bibliotecas necessárias
import os
import csv
import time
import pandas as pd
import json
from pip._vendor import requests
from datetime import date
import ast

# URL da API do BACEN - Quantidade e valor total das transações realizadas diariamente desde o primeiro dia de operações;
# from gen.venv.request_transc_24h import listaHorarios

url = 'https://olinda.bcb.gov.br/olinda/servico/SPI/versao/v1/odata/PixLiquidadosAtual?$top=10000&$orderby=Data%20asc&$format=json&$select=Data,Quantidade,Total'
request = requests.get(url=url)
info = json.loads(request.content)

# Data frame para JSON
df = pd.read_json(url)
df.to_csv(".\\sheets\\trans_diarias.csv") # Armazena o csv em subpasta sheet

arquivo_csv = pd.read_csv(".\\sheets\\trans_diarias.csv")
print(arquivo_csv.head())  # imprime top 5 linhas do arquivo trans_diarias.csv

########

# Exibir as colunas do arquivo importado
# print(arquivo_csv.info())

# adicionando colunas
arquivo_csv['Data'] = ""
arquivo_csv['Quantidade'] = ""
arquivo_csv['Total'] = ""

# criando lista de dados
listaDatas = []
listaQuantidade = []
listaTotal = []

for cadaLinha in arquivo_csv['value']:
    dicionario = ast.literal_eval(cadaLinha)  # converter string do value para dictionary
    listaDatas.append(dicionario["Data"])
    listaQuantidade.append(dicionario["Quantidade"])
    listaTotal.append(dicionario["Total"])

dados =\
    {
    'Data': listaDatas,
    'Quantidade': listaQuantidade,
    'Total': listaTotal
    }

df = pd.DataFrame(dados)
df.to_csv('.\\sheets\\trans_diarias-trat.csv', mode='w', index=False, header=True)  # Arquivos como nome final trat
# Modo w realiza sobrescrita dos dados;
# indica que este arquivo é o tratamento de um anterior;
print("Arquivo criado com sucesso!")
