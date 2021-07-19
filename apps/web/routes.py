from flask.json import jsonify
from . import web
from flask import request
from .models import *
from sqlalchemy import exc
from sqlalchemy.orm.exc import UnmappedInstanceError
@web.route('/', methods=['POST'])
def create_task():
    titulo=request.json['titulo']
    descripcion=request.json['descripcion']
    nueva_tarea=Task(titulo, descripcion)
    
    try:
        db.session.add(nueva_tarea)
        db.session.commit()
    except exc.IntegrityError as error:
        db.session.rollback()  
        return jsonify({'error':'Elemento duplicado'})
    return taskchema.jsonify(nueva_tarea)



@web.route('/task/<int:id>/', methods=['GET'])
def get_task(id):
    obj_task=Task.query.get(id)
    return taskchema.jsonify(obj_task)

@web.route('/task/update/<int:id>/', methods=['PUT'])
def update_task(id):
    obj_task=Task.query.get(id)
    titulo=request.json['titulo']
    descripcion=request.json['descripcion']
    obj_task.nombre=titulo
    obj_task.descripcion=descripcion
    db.session.commit()
    return taskchema.jsonify(obj_task)

@web.route('/tasks/', methods=['GET'])
def all_task():
    obj_task=Task.query.all()    
    return taskschema.jsonify(obj_task)


@web.route('/task/delete/<int:id>/', methods=['DELETE'])
def delete_task(id):  
    try:
        obj_task=Task.query.get(id)
        db.session.delete(obj_task)
        db.session.commit()
    except UnmappedInstanceError as error:
        return jsonify({'error':f'El ID:{id} no existe'})
    return taskchema.jsonify(obj_task)