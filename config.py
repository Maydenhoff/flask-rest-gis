import os
from dotenv import load_dotenv

load_dotenv()  

def str_to_bool(value):
    return value.lower() in ('true', '1', 't')


class Config:

    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = str_to_bool(os.getenv('DB_TRACK_MODIFICATIONS', 'True'))
