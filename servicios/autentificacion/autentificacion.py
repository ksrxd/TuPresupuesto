from datos.modelos import usuario as modelo_usuario
from datetime import datetime

#### el _ al comienzo de la funcion por convencion significa que es privada ######

#verificacion de la existecia del usuario
def _existe_usuario(NombreDeUsuario, Clave):
    usuarios = modelo_usuario.obtener_usuarios_por_nombre_clave(NombreDeUsuario, Clave)
    return not len(usuarios) == 0

#creacion de la sesion de usuario
def _crear_sesion(id_usuario):
    hora_actual = datetime.now()
    # dd/mm/yy H:M:S
    dt_string = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    return modelo_usuario.crear_sesion(id_usuario, dt_string)

#obtener usuarios

def obtener_usuarios():
    return modelo_usuario.obtener_usuarios()

# obtener usuario especifico

def obtener_usuario(id_usuario):
    usuarios = modelo_usuario.obtener_usuario(id_usuario)
    if len(usuarios) == 0:
        raise Exception("El nombre de usuario no existe")
    return usuarios[0]

# creacion de usuario
def crear_usuario(NombreDeUsuario, Clave):
    if not _existe_usuario(NombreDeUsuario, Clave):
        modelo_usuario.crear_usuario(NombreDeUsuario, Clave)
    else:
        raise Exception("El usuario ya existe")

# modificacion de entidad usuario

def modificar_usuario(id_usuario, datos_usuario):
    modelo_usuario.modificar_usuario(id_usuario, datos_usuario)

# borrar un usuario

def borrar_usuario(id_usuario):
    modelo_usuario.borrar_usuario(id_usuario)

# login

def login(NombreDeUsuario, Clave):
    if _existe_usuario(NombreDeUsuario, Clave):
        usuario = modelo_usuario.obtener_usuarios_por_nombre_clave(NombreDeUsuario, Clave)[0]
        return _crear_sesion(usuario['Id'])
    else:
        raise Exception("El usuario no existe o la clave no es correcta")

# validar sesion

def validar_sesion(id_sesion):
    sesiones = modelo_usuario.obtener_sesion(id_sesion)
    if len(sesiones) == 0:
        return False
    elif (datetime.now() - datetime.strftime(sesiones[0]['fecha_hora'], "%d/%m/%Y %H:%M:%S")).total_seconds() > 60:
        #sesion expirada
        return False
    else:
        return True

