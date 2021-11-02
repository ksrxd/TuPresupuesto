from flask import Flask, request, redirect, url_for
from flask import render_template
from web.servicios import autenticacion
from web.servicios import movimientos

app = Flask(__name__)


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

@app.route('/movimientos', methods=['GET', 'POST'])
def ingresar_movimientos():
    error = None
    if request.method == 'POST':
        if not movimientos.ingresar_movimientos(request.form['Fecha'], request.form['TipoMovimiento'], request.form['Concepto'], request.form['Categoria'], request.form['Monto']):
            error = 'No se pudo registar el movimiento'
        else:
            return redirect(url_for('ingresar_movimientos'))
    return render_template('movimientos.html', error = error)

@app.route('/ver_movimientos', methods=['GET', 'POST'])
def ver_movimientos():
    obtenermovi = movimientos.obtener_movimientos()
    return render_template('ver_movimientos.html', movimientos = obtenermovi)


if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
