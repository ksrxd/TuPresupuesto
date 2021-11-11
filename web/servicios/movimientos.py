import requests

from web.servicios import rest_api

#registro de movimientos y conexion con API
def ingresar_movimientos(Fecha, TipoMovimiento, Concepto, Categoria, Monto):
    body = {"Fecha": Fecha,
            "TipoMovimiento": TipoMovimiento,
            "Concepto": Concepto,
            "Categoria": Categoria,
            "Monto": Monto}
    respuesta = requests.post(f'{rest_api.API_URL}/movimientos', json=body)
    return respuesta.status_code == 200

# obtener movimientos

def obtener_movimientos():
    respuesta = requests.get(f'{rest_api.API_URL}/movimientos')
    return respuesta.json()

#obtener movimientos por <tipo>

def obtener_movimiento_tipomovimientoingreso():
    respuestatipomoviingreso = requests.get(f'{rest_api.API_URL}/movimientos/Ingreso')
    return respuestatipomoviingreso.json()

def obtener_movimiento_tipomovimientogasto():
    respuestatipomovigasto = requests.get(f'{rest_api.API_URL}/movimientos/Gasto')
    return respuestatipomovigasto.json()

# obtener el monto total de los movimientos

def obtener_total_gastos():
    respuestatotalgastos = requests.get(f'{rest_api.API_URL}/movimientos/montogastos')
    return respuestatotalgastos.json()

def obtener_total_ingresos():
    respuestatotalingresos = requests.get(f'{rest_api.API_URL}/movimientos/montoingresos')
    return respuestatotalingresos.json()