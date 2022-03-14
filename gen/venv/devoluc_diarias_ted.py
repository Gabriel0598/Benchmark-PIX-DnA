# Importação das bibliotecas necessárias
import os
import csv
import time
import pandas as pd
import json
from pip._vendor import requests
import ast

# URL da API do BACEN - Volume e valor total das transações realizadas por TED desde 2002;
url = 'https://olinda.bcb.gov.br/olinda/servico/STR/versao/v1/odata/TEDEvolucaoDiaria?$top=10000&$orderby=Data%20asc&$format=json&$select=Data,Quantidade,Total'
request = requests.get(url=url)
info = json.loads(request.content)

# Data frame para leitura do JSON
df = pd.read_json(url)
df.to_csv(".\\sheets\\trans_TED_overall.csv")  # Armazena o csv em subpasta sheet

# Variável para receber a planilha semi-estruturada:
arquivo_csv = pd.read_csv(".\\sheets\\trans_TED_overall.csv")
print(arquivo_csv.head())  # imprime top 5 linhas do arquivo trans_TED_overall.csv

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
    valorReaisEmMil = float(round(dicionario["Total"] * 1000, 2))
    listaTotal.append(valorReaisEmMil)

dados = \
{
    'Data': listaDatas,
    'Quantidade': listaQuantidade,
    'Total': listaTotal
}

df = pd.DataFrame(dados)
# Realiza tratamento das colunas do arquivo:
df.to_csv(".\\sheets\\trans_TED_overall_trat_.csv", mode='w', index=False, header=True)
# Arquivos como nome final trat
# Modo w realiza sobrescrita dos dados/ verificar utilização de modo append para evitar sobrescrição ou variável para data;
# indica que este arquivo é o tratamento de um anterior;
print("Arquivo criado com sucesso!")
