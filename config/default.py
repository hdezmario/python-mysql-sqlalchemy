
from os.path import abspath, dirname
from datetime import timedelta

# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''
class DefaultConfig:
    BASE_DIR = dirname(dirname(abspath(__file__)))
    SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    # CONFIGURACION DE FLASK-JWT-EXTENDED 
    # JWT_TOKEN_LOCATION=["cookies"]
    # si la conexion es por https poner en true 
    JWT_COOKIE_SECURE=False
    JWT_SECRET_KEY="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoicGF5bG9hZCJ9.Joh1R2dYzkRvDkqv3sygm5YyK8Gi4ShZqbhK2gxcs2U"  # Change this!
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=3)

    #  CONFIGURACION DE BASE DE DATOS
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS=False


