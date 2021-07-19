from apps.usuario.models import Usuario

def autentificacion(username, password):
    user = Usuario.query.filter_by(usuario=username, password=password).first()
    return user



