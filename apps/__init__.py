from flask import Flask
from .web import web as webpackage
from apps.web.models import db as db_web, ma as ma_web

from apps.usuario import usuario as user_blueprint
from apps.usuario.models import db as db_user, ma as ma_user

from flask_jwt_extended import JWTManager

def create_app(settings_module):
    # CREAMOS LA INSTANCIA DE NUESTRA APLICACION 
    app = Flask(__name__, instance_relative_config=True)
    # APLICAMOS CONFIGURACIONES DE LA APICACION
    app.config.from_object(settings_module)

    # INICIALIZAMOS JWT
    jwt = JWTManager(app)

    # INICIALIZAMOS LAS BASE DE DATOS DE LAS APLICACIONES
    db_web.init_app(app)
    db_user.init_app(app)
    with app.app_context():
        db_web.create_all()
        db_user.create_all()

    # INICIALIZAMOS LOS SCHEMAS DE MODELOS
    ma_web.init_app(app)
    ma_user.init_app(app)


    # REGISTRAMOS Blueprint DE NUESTROS PAQUETES
    app.register_blueprint(webpackage)
    app.register_blueprint(user_blueprint)

    return app