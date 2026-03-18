from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    mysql_host: str 
    mysql_user: str 
    mysql_password: str
    mysql_port: str 
    mysql_name: str 
    
    postgres_host: str
    postgres_user: str
    postgres_password: str
    postgres_port: str
    postgres_name: str

    model_config = SettingsConfigDict(env_file=".env")


config = Config()