from datos.base_de_datos import BaseDeDatos
# querys sql

#query obtencion ususario especifico
def obtener_usuario(id_usuario):
    obtener_usuarios_sql = f"""
        SELECT Id, NombreDeUsuario, CorreoElectronico, Rol
        FROM Usuarios
        WHERE ID = {id_usuario}
    """
    bd = BaseDeDatos()
    return [{"Id": registro[0],
             "NombreDeUsuario": registro[1],
             "CorreoElectronico": registro[2],
             "Rol":registro[3]
             } for registro in bd.ejecutar_sql(obtener_usuarios_sql)]

#query obtencion lista de usuarios
def obtener_usuarios():
    obtener_usuarios_sql = f"""
        SELECT Id, NombreDeUsuario, CorreoElectronico, Rol
        FROM Usuarios
    """
    bd = BaseDeDatos()
    return [{"Id": registro[0],
             "NombreDeUsuario": registro[1],
             "CorreoElectronico": registro[2],
             "Rol":registro[3]
             } for registro in bd.ejecutar_sql(obtener_usuarios_sql)]

# query crear usuario
def crear_usuario(NombreDeUsuario, Clave):
    crear_usuario_sql = f"""
        INSERT INTO Usuarios(NombreDeUsuario, Clave)
        VALUES ('{NombreDeUsuario}', '{Clave}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)

#query modficacion usuario
def modificar_usuario(id_usuario, datos_usuario):
    modificar_usuario_sql = f"""
        UPDATE Usuarios
        SET NombreDeUsuario ='{datos_usuario["NombreDeUsuario"]}', Clave = '{datos_usuario["Clave"]}'
        WHERE Id = '{id_usuario}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_usuario_sql)

#query para obtener usuarios por nombre y clave
def obtener_usuarios_por_nombre_clave(NombreDeUsuario, Clave):
    obtener_usuario_sql = f"""
        SELECT Id, NombreDeUsuario, Rol
        FROM Usuarios
        WHERE NombreDeUsuario = '{NombreDeUsuario}' and Clave = '{Clave}'
    """
    bd = BaseDeDatos()
    return [{"Id": registro[0],
             "NombreDeUsuario": registro[1],
             "Rol": registro[2]
             } for registro in bd.ejecutar_sql(obtener_usuario_sql)]

# query borrar usuario

def borrar_usuario(id_usuario):
    obtener_usuarios_sql = f"""
        DELETE FROM Usuarios
        WHERE Id = {id_usuario}
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(obtener_usuarios_sql)

# query crear sesion
def crear_sesion(id_usuario, dt_string):
    crear_sesion_sql = f"""
                INSERT INTO Sesiones(id_usuario, fecha_hora)
                VALUES ('{id_usuario}', '{dt_string}')
            """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(crear_sesion_sql, True)

# query obtencion de sesion

def obtener_sesion(id_sesion):
    obtener_sesion_sql = f"""
        SELECT Id, id_usuario, fecha_hora FROM Sesiones WHERE ID = {id_sesion}
    """
    bd = BaseDeDatos()
    return [{"Id": registro[0],
             "id_usuario": registro[1],
             "fecha_hora": registro[2]}
            for registro in bd.ejecutar_sql(obtener_sesion_sql)]

