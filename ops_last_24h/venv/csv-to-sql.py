import psycopg2
import psycopg2.extras
import pandas as pd

# Devido a problemas de privilégios de ADM não foi possível realizar automatização da criação de tabelas

conn = psycopg2.connect(database="dcduom29m2ara1", user='ewyfsavzuwidwg',
                        password='1471510470ddebb0fc2f0befd4a88b01e256bf521f46f6347fae0f1142f64c1c',
                        host='ec2-44-192-245-97.compute-1.amazonaws.com', port='5432')

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
