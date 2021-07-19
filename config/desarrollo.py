from .default import *
# Parámetros para activar el modo debug
class Configuracion(DefaultConfig):
    TESTING = True
    DEBUG = True
    APP_ENV = APP_ENV_DEVELOPMENT
    SQLALCHEMY_DATABASE_URI = 'mysql://root:S1st3m45@127.0.0.1/flask_tuto'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    # SQLALCHEMY_BINDS = {
    #     'database': 'mysql://root:S1st3m45@localhost/flask_tuto'
    # }
    