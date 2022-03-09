# Importação das bibliotecas necessárias
import os
import csv
import time
import pandas as pd
import json
from pip._vendor import requests
from datetime import date
import ast
import datetime

# URL da API do BACEN - Volume e valor total das transações realizadas nas últimas 24h;
# Consulta inicial em 03/08/2022 as 09h17
url = 'https://olinda.bcb.gov.br/olinda/servico/SPI/versao/v1/odata/PixLiquidadosIntradia?$top=1000&$format=json&$select=Horario,QuantidadeMedia,TotalMedio'
request = requests.get(url=url)
info = json.loads(request.content)

# Captura de data em variável
data_atual = date.today()
print(data_atual)

# Data frame para leitura do JSON
df = pd.read_json(url)
df.to_csv(".\\sheets\\trans_last_24h_" + str(data_atual) + ".csv")  # Armazena o csv em subpasta sheet com data atualizada

# Variável para receber a planilha semi-estruturada:
arquivo_csv = pd.read_csv(".\\sheets\\trans_last_24h_" + str(data_atual) + ".csv")
print(arquivo_csv.head())  # imprime top 5 linhas do arquivo trans_last_24h.csv

# Exibir as colunas do arquivo importado
# print(arquivo_csv.info())

# adicionando colunas
arquivo_csv['Horario'] = ""
arquivo_csv['QuantidadeMedia'] = ""
arquivo_csv['TotalMedio'] = ""

# criando lista de dados
listaHorarios = []
listaQuantidadeMedia = []
listaTotalMedio = []

for cadaLinha in arquivo_csv['value']:
    dicionario = ast.literal_eval(cadaLinha)  # converter string do value para dictionary
    listaHorarios.append(dicionario["Horario"])
    listaQuantidadeMedia.append(dicionario["QuantidadeMedia"])
    listaTotalMedio.append(dicionario["TotalMedio"])

dados = {
    'Horario': listaHorarios,
    'QuantidadeMedia': listaQuantidadeMedia,
    'TotalMedio': listaTotalMedio
}

df = pd.DataFrame(dados)
# Realiza tratamento das colunas do arquivo:
df.to_csv(".\\sheets\\trans_last_24h_trat_" + str(data_atual) + ".csv", mode='w', index=False, header=True)
# Arquivos como nome final trat
# Modo w realiza sobrescrita dos dados/ verificar utilização de modo append para evitar sobrescrição ou variável para data;
# indica que este arquivo é o tratamento de um anterior;
print("Arquivo criado com sucesso!")
