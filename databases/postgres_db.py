from sqlalchemy import create_engine
from .config import config 

try:
    postgres_engine = create_engine(
        f"postgresql+psycopg2://{config.postgres_user}:{config.postgres_password}@{config.postgres_host}:{config.postgres_port}/{config.postgres_name}"
        )
    print('Conexão com PostgreSQL criada')
except Exception as e:
    print(e)