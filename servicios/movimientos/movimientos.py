from datos.modelos import movimientos as modelo_movimientos

def ingresar_movimientos(Fecha, TipoMovimiento, Concepto, Categoria, Monto):
    modelo_movimientos.ingresar_movimientos(Fecha, TipoMovimiento, Concepto, Categoria, Monto)

def eliminar_movimientos(Id):
    modelo_movimientos.eliminar_movimientos(Id)

def modificar_movimientos(Id, datos_usuario):
    modelo_movimientos.modificar_movimientos(Id, datos_usuario)

#obtener movimiento especifico
def obtener_movimiento(Id):
        movimiento = modelo_movimientos.obtener_movimiento(Id)
        if len(movimiento) == 0:
            raise Exception("El movimiento no existe")
        return movimiento[0]

#obtener todos los movimientos

def obtener_movimientos():
    return modelo_movimientos.obtener_movimientos()

#obtener movimientos por TipoMovimiento

def obtener_movimiento_tipomovimento(TipoMovimiento):
    return modelo_movimientos.obtener_movimientos_por_tipo(TipoMovimiento)


