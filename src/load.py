import pandas as pd
from databases.postgres_db import postgres_engine
from databases.mysql_db import mysql_engine
from sqlalchemy import *
from datetime import datetime as dt

metadata = MetaData()
clients = Table('clients', metadata, autoload_with=mysql_engine) #Pega a tabela do mysql

def load_db(df):
    '''Pega os dados filtrados, e coloca em um novo database (MySql)'''
    with mysql_engine.connect() as conn:
        try:
            records = df.to_dict(orient='records') #Transforma o dataframe em dicionario
            stmt = insert(clients).values(records)
            result = conn.execute(stmt)
            conn.commit()
            
            return f'Importação concluída! \n{result.rowcount} usuários cadastrados com sucesso!'
        except Exception as e:
            print(f'Error: {e}')