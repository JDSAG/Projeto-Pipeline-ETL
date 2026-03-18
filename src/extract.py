import pandas as pd
from databases.postgres_db import postgres_engine
from databases.mysql_db import mysql_engine
from sqlalchemy import *
from datetime import datetime as dt
# Extrair os dados do postgres 
SELECT_RAW_TABLE = '''SELECT * FROM raw_clients'''


def extract_db(CONN):
    '''Extrai o database Postgres'''
    try:
        extract_table = pd.read_sql_query(SELECT_RAW_TABLE,CONN) 
        #print(f"Dados extraidos com sucesso {extract_table.info()}")
        return extract_table
    except Exception as e:
        print(f'Error: {e}')