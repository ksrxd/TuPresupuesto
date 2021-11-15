from flask import Flask, request, redirect, json, url_for
from flask import render_template
from web.servicios import autenticacion
from web.servicios import movimientos
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not autenticacion.validar_credenciales(request.form['login'], request.form['password']):
            error = 'Credenciales inválidas'
        else:
            return redirect(url_for('inicio'))
    return render_template('login.html', error=error)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':
        if not autenticacion.crear_usuario(request.form['login'], request.form['password']):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('inicio'))
    return render_template('registro.html', error=error)


@app.route('/inicio')
def inicio():
    usuarios = autenticacion.obtener_usuarios()
    return render_template('inicio.html', usuarios=usuarios)

@app.route('/acercade')
def acercade():
    return render_template('acercade.html')

@app.route('/movimientos', methods=['GET', 'POST'])
def ingresar_movimientos():
    error = None
    if request.method == 'POST':
        if not movimientos.ingresar_movimientos(request.form['Fecha'], request.form['TipoMovimiento'], request.form['Concepto'], request.form['Categoria'], request.form['Monto']):
            error = 'No se pudo registar el movimiento'
        else:
            return redirect(url_for('ingresar_movimientos'))
    if request.method == 'GET':
        tmovimientos = movimientos.obtener_movimientos()
        return render_template('movimientos.html', movimientos=tmovimientos)
    return render_template('movimientos.html', error = error)

@app.route('/movimientos/<Id>')
def borrar_movimiento(Id):
    bmovimientos = movimientos.borrar_movimiento(Id)
    return render_template('movimientos.html', movimientos = bmovimientos)
# tablas en movimientos.html
@app.route('/movimientos', methods=['GET'])
def tablas_movimientos():
    tmovimientos = movimientos.obtener_movimientos()
    return render_template('movimientos.html', tmovimientos = tmovimientos)

@app.route('/ver_movimientos', methods=['GET', 'POST'])
def ver_movimientos():
    obtenermovi = movimientos.obtener_movimientos()
    return render_template('ver_movimientos.html', movimientos = obtenermovi)
@app.route('/ver_movimientos', methods=['GET'])
def obtener_moviportipoingreso():
    obtenermoviportipoingreso = movimientos.obtener_movimiento_tipomovimientoingreso()
    return render_template('ver_movimientos.html', movimientos = obtenermoviportipoingreso)
@app.route('/ver_movimientos', methods=['GET'])
def obtener_moviportipogasto():
    obtenermoviportipogasto = movimientos.obtener_movimiento_tipomovimientogasto()
    return render_template('ver_movimientos.html', movimientos = obtenermoviportipogasto)

# mostrar montos totales
@app.route('/inicio', methods=['GET', 'POST'])
def obtener_montototalingresos():
    obtenermontototalingresos = movimientos.obtener_total_ingresos()
    return render_template('inicio.html', ingresos = obtenermontototalingresos)


if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)

