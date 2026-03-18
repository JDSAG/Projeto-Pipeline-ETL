#from databases.mysql_db import engine_mysql
from databases.postgres_db import postgres_engine
from src.extract import extract_db
from src.transform import *
from src.load import load_db

#Extract
postgres_extract = extract_db(postgres_engine)

#Transform
postgres_transform = column_checker(postgres_extract)
postgres_validation = validations(postgres_transform)

#Load
convert_db = load_db(postgres_validation)