import pandas as pd
from databases.postgres_db import postgres_engine
from databases.mysql_db import mysql_engine
from sqlalchemy import *
from datetime import datetime as dt
import re

def column_checker(df):
    '''Essa função deverá checar e transformar os seguintes problemas:
        Nomes com espaços extras ou capitalização inconsistente
        Registros incompletos
        Campos nulos (nome ou email)'''
    print(f'Registros extraidos {len(df)}')
    try:
        df['nome'] = df['nome'].str.strip().str.capitalize()
        nan_checker = df.dropna(subset=['nome','email'])
        print(f'Registros nulos removidos: {len(nan_checker)} Registros extraidos.')
        return nan_checker
    except Exception as e:
        print(f'Error: {e}')
        

def validations(table):
    '''Essa função deverá realizar as seguintes validações:
        Emails em formato inválido
        Telefones com valores inválidos
        Remove Duplicatas'''
    #Padrões
    PATTERN_NUMBER = r"^85\d{8}$"
    PATTERN_EMAIL = r'^[a-zA-Z0-9.-]+@[a-zA-Z]+\.[a-z]{2,}$'
    
    invalid_email = []
    invalid_phone = []
    
    for i in table['email']:
        email_validation = re.fullmatch(PATTERN_EMAIL,i) 
        if not email_validation:
            invalid_email.append(i) #Coloca todos os emails invalidos numa lista

    print(f'Emails Inválidos:{len(invalid_email)}') #Verificação teste
    validated_email_table = table[~table['email'].isin(invalid_email)] #Remove todas as tuplas onde o email está invalido
    
    # Verificação de telefone
    
    for i in validated_email_table['telefone']:
        if i:
            number_validation = re.fullmatch(PATTERN_NUMBER,i) 
            if not number_validation:
                invalid_phone.append(i)
            
    print(f'Telefones Inválidos:{len(invalid_phone)}') #Verificação teste
    validated_table = validated_email_table[~validated_email_table['telefone'].isin(invalid_phone)]
    
    validated_table = validated_table.drop_duplicates(subset=['email'])#Dropar duplicatas pós validação
    
    print(f'Registros válidos: {len(validated_table)}')
    return validated_table
