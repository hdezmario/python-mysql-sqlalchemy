from flask.json import jsonify
from . import usuario
from flask import request
from apps.usuario.jwt_user import autentificacion
from apps.usuario.models import usuarioSchema
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required



@usuario.route('/usuario/login/', methods=['POST'])
def user_index():
    user=request.json['user']
    passw=request.json['pass']    
    user_obj=autentificacion(user, passw)
    if user_obj == None:
        return jsonify({"msg": "Bad username or password"}), 401
    else:
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token)


@usuario.route('/user/dashboard')
@jwt_required()
def user_dashboard():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
    