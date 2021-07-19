from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
from flask_marshmallow import Marshmallow


db=SQLAlchemy()
ma=Marshmallow()


class Usuario(db.Model):
    id=Column(Integer, primary_key=True)
    usuario=Column(String(30), unique=True)
    password=Column(String(200))
    # def __init__(self, titulo, descripcion):
    #     self.nombre=titulo
    #     self.descripcion=descripcion



class UsuarioSchema(ma.Schema):
    class Meta:
        fields=(
            'id',
            'usuario',
            'password',
        )

usuarioSchema=UsuarioSchema()
usuariosSchema=UsuarioSchema(many=True)