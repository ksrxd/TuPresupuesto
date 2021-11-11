from datos.base_de_datos import BaseDeDatos

def ingresar_movimientos(Fecha, TipoMovimiento, Concepto, Categoria, Monto):
    ingresar_movimientos_sql = f"""
        INSERT INTO Movimientos(Fecha, TipoMovimiento, Concepto, Categoria, Monto)
        VALUES ('{Fecha}', '{TipoMovimiento}', '{Concepto}', '{Categoria}', '{Monto}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(ingresar_movimientos_sql)

def eliminar_movimientos(Id):
    eliminar_movimientos_sql = f"""
        DELETE FROM Movimientos 
        WHERE Id = {Id}
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_movimientos_sql)

### Fecha, TipoMovimiento, Concepto, Categoria, Monto
def modificar_movimientos(Id, datos_usuario):
    modificar_movimientos_sql = f"""
        UPDATE Movimientos
        SET Fecha = '{datos_usuario["Fecha"]}', TipoMovimiento = '{datos_usuario["TipoMovimiento"]}', Concepto= '{datos_usuario["Concepto"]}', Categoria = '{datos_usuario["Categoria"]}', Monto = '{datos_usuario["Monto"]}'
        WHERE Id = '{Id}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_movimientos_sql)

# obtener movimiento por categoria

def obtener_movimiento_por_categoria(Categoria):
    obtener_movimientos_sql = f"""
        SELECT Id, Fecha, TipoMovimiento, Concepto, Categoria, Monto
        FROM Movimientos
        WHERE Categoria = '{Categoria}'
    """
    bd = BaseDeDatos()
    return [{"Id": registro[0],
             "Fecha": registro[1],
             "TipoMovimiento": registro[2],
             "Concepto": registro[3],
             "Categoria": registro[4],
             "Monto": registro[5]
             } for registro in bd.ejecutar_sql(obtener_movimientos_sql)]
# obtener movimientos por tipo de movimiento

def obtener_movimientos_por_tipo(TipoMovimiento):
    obtener_movimientos_sql = f"""
        SELECT Id, Fecha, TipoMovimiento, Concepto, Categoria, Monto
        FROM Movimientos
        WHERE TipoMovimiento = '{TipoMovimiento}'
    """
    bd = BaseDeDatos()
    return [{"Id": registro[0],
             "Fecha": registro[1],
             "TipoMovimiento": registro[2],
             "Concepto": registro[3],
             "Categoria": registro[4],
             "Monto": registro[5]
             } for registro in bd.ejecutar_sql(obtener_movimientos_sql)]

#query obtencion todos los movimientos
def obtener_movimientos():
    obtener_movimientos_sql = f"""
        SELECT Id, Fecha, TipoMovimiento, Concepto, Categoria, Monto
        FROM Movimientos
    """
    bd = BaseDeDatos()
    return [{"Id": registro[0],
             "Fecha": registro[1],
             "TipoMovimiento": registro[2],
             "Concepto": registro[3],
             "Categoria": registro[4],
             "Monto": registro[5]
             } for registro in bd.ejecutar_sql(obtener_movimientos_sql)]

# obtener todos los montos

def obtener_montototal_gasto():
    obtener_montototal_gasto_sql = f"""
        SELECT SUM(Monto)
        FROM Movimientos
        WHERE TipoMovimiento = 'Gasto'
    """
    bd = BaseDeDatos()
    return [{"Gastos totales": registro[0]}
            for registro in bd.ejecutar_sql(obtener_montototal_gasto_sql)]

def obtener_montototal_ingreso():
    obtener_montototal_ingreso_sql = f"""
        SELECT SUM(Monto)
        FROM Movimientos
        WHERE TipoMovimiento = 'Ingreso'
    """
    bd = BaseDeDatos()
    return [{"Ingresos totales": registro[0]}
            for registro in bd.ejecutar_sql(obtener_montototal_ingreso_sql)]

