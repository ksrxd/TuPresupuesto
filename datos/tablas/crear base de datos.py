import sqlite3

#creo conexion con db

conectar = sqlite3.connect('../../tupresupuesto.db')
#creo tablas
conectar.execute('CREATE TABLE Usuarios(Id INTEGER PRIMARY KEY, NombreDeUsuario TEXT NOT NULL, CorreoElectronico TEXT, Clave TEXT NOT NULL, Rol INTEGER)')
conectar.execute('CREATE TABLE Movimientos(Id INTEGER PRIMARY KEY, Fecha INTEGER, TipoMovimiento TEXT NOT NULL, Concepto TEXT NOT NULL, Categoria TEXT NOT NULL, Monto FLOAT NOT NULL )')
conectar.execute('CREATE TABLE Limite_Mensual(Mes_año INTEGER PRIMARY KEY, Monto FLOAT NOT NULL)')

#creo tablas de relacion
# relacion entre tabla usuario y tabla Movimientos
conectar.execute('CREATE TABLE Usuario_Movimientos(NombreDeUsuario_Usuario TEXT NOT NULL, Id_Movimientos INTEGER NOT NULL, FOREIGN KEY(NombreDeUsuario_Usuario) REFERENCES Usuarios(NombreDeUsuario), FOREIGN KEY(Id_Movimientos) REFERENCES Movimientos(Id))')
# relacion entre tabla Movimientos y Limite_Mensual
conectar.execute('CREATE TABLE Limite_Gastos(Fecha_LimiteGastos INTEGER NOT NULL, Monto_Limite TEXT NOT NULL, FOREIGN KEY(Fecha_LimiteGastos) REFERENCES Movimientos(Id), FOREIGN KEY(Monto_Limite) REFERENCES Limite_Mensual(Mes_año))')
# Tabla sesiones
conectar.execute('CREATE TABLE Sesiones(Id INTEGER PRIMARY KEY, id_usuario TEXT, fecha_hora TEXT, FOREIGN KEY(id_usuario) REFERENCES Usuarios(Id))')


#cierro conexion
conectar.close()