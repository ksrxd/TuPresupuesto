from flask import Flask, request, session, jsonify
from servicios.autentificacion import autentificacion
from servicios.movimientos import movimientos
from flask import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#index
@app.route('/')
def get_index():
    titulo_tupresupuesto = 'TuPresupuesto'
    return render_template('index.html', titulo=titulo_tupresupuesto)

#creacion de usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    # llamar al servicio de autentifacion
    datos_usuario = request.get_json()
    if 'NombreDeUsuario' not in datos_usuario:
        return 'El nombre de usuario es requerido', 412
    if 'Clave' not in datos_usuario:
        return 'La clave es requerida', 412
    try:
        autentificacion.crear_usuario(datos_usuario['NombreDeUsuario'], datos_usuario['Clave'])
    except Exception:
        return 'El usuario ya existe', 412
    return 'Usuario creado correctamente', 200

# modificar usuario
@app.route('/usuarios/<id_usuario>', methods=['PUT'])
def modificar_usuario(id_usuario):
    datos_usuario = request.get_json()
    if 'NombreDeUsuario' not in datos_usuario or datos_usuario['NombreDeUsuario'] == '':
        return 'El nombre de usuario es requerido', 412
    if 'Clave' not in datos_usuario:
        return 'La clave es requerida', 412
    autentificacion.modificar_usuario(id_usuario, datos_usuario)
    return 'Usuario modificado exitosamente', 200

#obtener lista completa de usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(autentificacion.obtener_usuarios())

# obtener usuario en especifico
@app.route('/usuarios/<id_usuario>', methods=['GET'])
def obtener_usuario(id_usuario):
    try:
        usuario = autentificacion.obtener_usuario(id_usuario)
        return jsonify(usuario)
    except Exception:
        return 'El usuario no fue encontrado', 404

# eliminar usuario
@app.route('/usuarios/<id_usuario>', methods=['DELETE'])
def borrar_usuario(id_usuario):
    autentificacion.borrar_usuario(id_usuario)
    return 'Usuario borrado exitosamente', 200

#login de usuario
@app.route('/login', methods=['POST'])
def login():
    datos_usuario = request.get_json()
    if 'NombreDeUsuario' not in datos_usuario:
        return 'Se requiere el nombre de usuario', 412
    if 'Clave' not in datos_usuario:
        return 'Se requiere la clave', 412
    try:
        id_sesion = autentificacion.login(datos_usuario['NombreDeUsuario'], datos_usuario['Clave'])
        return jsonify({"id_sesion": id_sesion})
    except Exception:
        return 'El usuario no ha sido encontrado', 404

########## ENDPOINTS MOVIMIENTOS ##############
#creacion de movimientos
@app.route('/movimientos', methods=['POST'])
def ingresar_movimientos():
    registro_movimientos = request.get_json()
    movimientos.ingresar_movimientos(registro_movimientos['Fecha'], registro_movimientos['TipoMovimiento'], registro_movimientos['Concepto'], registro_movimientos['Categoria'], registro_movimientos['Monto'])
    return 'Movimiento creado correctamente', 200

#eliminar un movimiento
@app.route('/movimientos/<Id>', methods=['DELETE'])
def eliminar_movimientos(Id):
    movimientos.eliminar_movimientos(Id)
    return 'Movimiento eliminado correctamente', 200

#modificar movimientos
@app.route('/movimientos/<Id>', methods=['PUT'])
def modificar_movimientos(Id):
    datos_usuario = request.get_json()
    movimientos.modificar_movimientos(Id, datos_usuario)
    return 'Movimiento modificado correctamente', 200

#obtener listado de movimientos
@app.route('/movimientos', methods=['GET'])
def obtener_movimientos():
    return jsonify(movimientos.obtener_movimientos())

#obtener movimientos por categoria ####
@app.route('/movimientos/<TipoMovimiento>', methods=['GET'])
def obtener_movimientos_por_tipo(TipoMovimiento):
    return jsonify(movimientos.obtener_movimiento_tipomovimento(TipoMovimiento))

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)