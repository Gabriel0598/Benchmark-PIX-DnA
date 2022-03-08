# Importação das bibliotecas necessárias
import os
import csv
import time
import pandas as pd
import json
from pip._vendor import requests
from datetime import date

# URL da API do BACEN - Volume e valor total das transacoes realizadas nas ultimas 24h;
# Consulta inicial em 03/08/2022 as 09h17
url = 'https://olinda.bcb.gov.br/olinda/servico/SPI/versao/v1/odata/PixLiquidadosIntradia?$top=1000&$format=json&$select=Horario,QuantidadeMedia,TotalMedio'
request = requests.get(url=url)
info = json.loads(request.content)

# df = pd.json_normalize(info['Horario'])
df = pd.read_json(url)
df.to_csv("teste.csv")

# tran_diarias = request.json()
# print(request.content)

# print('Horario: {}'.format(tran_diarias['Horario']))
# Criacao do Dataframe, definicao do nome das Colunas e datatype
# df = pd.DataFrame(list(obj.items('Horario')),columns=['horario', 'quantmedia', 'valor_totmedio'], dtype=str)
# df.id = df.preco.astype(str)



"""
# Captura de dados, novo tutorial
def buscar_dados():
    request = requests.get("https://olinda.bcb.gov.br/olinda/servico/SPI/versao/v1/odata/PixLiquidadosIntradia?$top=1000&$format=json&$select=Horario,QuantidadeMedia,TotalMedio")
    todos = json.loads(request.content)
    # print(request.content)
    print(todos)
    print(todos['titulo'])
    
    if _name_ == 'api_request':
        buscar_dados()
"""