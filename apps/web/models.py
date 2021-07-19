from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db=SQLAlchemy()
ma=Marshmallow()


class Task(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(70), unique=True)
    descripcion=db.Column(db.String(150))
    def __init__(self, titulo, descripcion):
        self.nombre=titulo
        self.descripcion=descripcion



class TaskSchema(ma.Schema):
    class Meta:
        fields=(
            'id',
            'nombre',
            'descripcion',
        )

taskchema=TaskSchema()
taskschema=TaskSchema(many=True)