from application_properties import obtener_conexion

#------------- Listar -------------
def listar():
    conexion = obtener_conexion()
    profesores = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, apellido, email, password, calificacion FROM profesor")
        profesores = cursor.fetchall()
    conexion.close()
    return profesores

#------------- Registrar -------------
def registro(nombre, apellido, email, password, calificacion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO profesor(nombre, apellido, email, password, calificacion) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, apellido, email, password, calificacion))
    conexion.commit()
    conexion.close()

#------------- Modificar -------------
def modificar(nombre, apellido, email, password, calificacion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE profesor SET nombre = %s, apellido = %s, email = %s, password = %s, calificacion = %s",
                       (nombre, apellido, email, password, calificacion))
    conexion.commit()
    conexion.close()

#------------- Eliminar -------------
def eliminar(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM profesor WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()