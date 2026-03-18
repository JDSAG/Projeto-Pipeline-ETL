from sqlalchemy import create_engine
from databases.config import config 

try:
    mysql_engine = create_engine(
    f'mysql://{config.mysql_user}:{config.mysql_password}@{config.mysql_host}:{config.mysql_port}/{config.mysql_name}')
    print("Conexão com MySQL criada")
except Exception as e:
    print (e)
