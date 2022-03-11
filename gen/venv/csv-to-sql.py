import psycopg2
import psycopg2.extras
import pandas as pd
import app_settings

# Devido a problemas de privilégios de ADM não foi possível realizar automatização da criação de tabelas

conn = app_settings.string_connection # Arquivo app_settings possui credenciais para acesso ao banco
# Banco de dados hospedado no Heroku

conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE db_trans_diarias_PIX(Id SERIAL PRIMARY KEY, Data date NOT NULL, Quantidade int, Total decimal);'''
# CREATE TABLE IF NOT EXISTS

sql2 = '''COPY db_trans_diarias_PIX(Data, Quantidade, Total)
FROM '/sheets/trans_diarias-trat.csv' DELIMITER ',' CSV HEADER;'''

cursor.execute(sql2)

sql3 = '''SELECT * FROM db_trans_diarias_PIX;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)

conn.commit()
conn.close()
