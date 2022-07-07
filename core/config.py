import os
from dotenv import load_dotenv
from pathlib import Path

#Lo primero que debemos hacer es ubicar donde esta nuestro .env
env_path = Path('.') / '.env' # Esto lo que hace es volver una carpeta atras donde esta el archivo .env
load_dotenv(dotenv_path=env_path) # Cargamos el archivo de .env a travez del env_path

class Settings:
    PROJECT_NAME:str = "PROYECTO-RECOLECCION-DATOS"
    PROJECT_VERSION:str = "1.0"
    URL_CINE:str = os.getenv('URL_CINE')
    URL_MUSEO:str = os.getenv('URL_MUSEO')
    URL_BIBLIOTECA:str = os.getenv('URL_BIBLIOTECA')
    POSTGRES_USER:str = os.getenv('POSTGRES_USER')
    POSTGRES_DB:str = os.getenv('POSTGRES_DB')
    POSTGRES_PASSWORD:str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER:str = os.getenv('POSTGRES_SERVER')
    POSTGRES_PORT:str = os.getenv('POSTGRES_PORT')
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"    

# Instanciamos settings
settings = Settings()