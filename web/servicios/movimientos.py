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

# obtener movimeintos

def obtener_movimientos():
    respuesta = requests.get(f'{rest_api.API_URL}/movimientos')
    return respuesta.json()