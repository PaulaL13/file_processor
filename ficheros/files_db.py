from database.db import *
from utils.logs import *

## FUNCIONES INSERTAR DATOS A LA BASE DE DATOS ##
#Creamos función para verificar si ya se ha procesado un fichero
def ficheros_ya_procesados(nombre_fichero):
    conexion = conectar_db()

    if conexion: 
        cursor = conexion.cursor()
        query = "SELECT COUNT(*) FROM sabadell_cabecera_fichero WHERE nombre_fichero = %s"
        try:
            cursor.execute(query, (nombre_fichero,))
            resultado = cursor.fetchone()[0]
            return resultado > 0
        except Exception as error:
            crearErrorLog(nombre_fichero, str(error))
        finally:
            cursor.close()
            conexion.close()

        
    else:
        crearErrorLog(nombre_fichero,"Error de conexion a mysql")

#Función para insertar datos cabecera fichero en la DB
def insertar_cabecera_fichero(cursor, tipo_registro, fecha_proceso, fecha_inicio, fecha_final, datos_adicionales, nombre_fichero, fila_completa):
    #cursor = conexion.cursor()

    query = """
    INSERT INTO sabadell_cabecera_fichero(tipo_registro, fecha_proceso, fecha_inicio, fecha_final, datos_adicionales, nombre_fichero, fila_completa)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    valores = (tipo_registro, fecha_proceso, fecha_inicio, fecha_final, datos_adicionales, nombre_fichero, fila_completa)
    cursor.execute(query, valores)

    #Obtenemos el ID de la fila insertada
    cabecera_fichero_id = cursor.lastrowid 

    return cabecera_fichero_id

#Función para insertar datos cabecera remesa en la DB
def insertar_cabecera_remesa(cursor, cabecera_fichero_id, tipo_registro, numero_contrato, numero_comercio, cuenta_comercio, oficina_gestora, fecha_proceso, fecha_inicio, fecha_final, datos_adicionales, fila_completa):
    #cursor = conexion.cursor()

    query = """
    INSERT INTO sabadell_cabecera_remesa(cabecera_fichero_id, tipo_registro, numero_contrato, numero_comercio, cuenta_comercio, oficina_gestora, fecha_proceso, fecha_inicio, fecha_final, datos_adicionales, fila_completa)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (cabecera_fichero_id, tipo_registro, numero_contrato, numero_comercio, cuenta_comercio, oficina_gestora, fecha_proceso, fecha_inicio, fecha_final, datos_adicionales, fila_completa)
    cursor.execute(query, valores)

#Función para insertar datos registro operacion en la DB
def insertar_registro_operacion(cursor, cabecera_fichero_id, tipo_registro, fecha_valoracion_abono, numero_remesa, numero_factura_operacion, oficina_remesa, tarjeta, clase_tarjeta, modalidad_pago, entidad_tarjeta_emisora, fecha_operacion, hora_operacion, numero_autorizacion, tipo_operacion, captura_operacion, importe_operacion, signo_operacion, tasa_descuento, importe_descuento, signo_descuento, importe_liquido, signo_liquido, numero_tpv, arn, tasa_intercambio, gastos, datos_adicionales, divisa_comercio, numero_operacion, codigo_razon, mas_datos_adicionales, importe_original, signo_original, divisa_original, incluso_mas_datos_adicionales, fila_completa):
    #cursor = conexion.cursor()

    query = """
    INSERT INTO sabadell_registro_operacion(cabecera_fichero_id, tipo_registro, fecha_valoracion_abono, numero_remesa, numero_factura_operacion, oficina_remesa, tarjeta, clase_tarjeta, modalidad_pago, entidad_tarjeta_emisora, fecha_operacion, hora_operacion, numero_autorizacion, tipo_operacion, captura_operacion, importe_operacion, signo_operacion, tasa_descuento, importe_descuento, signo_descuento, importe_liquido, signo_liquido, numero_tpv, arn, tasa_intercambio, gastos, datos_adicionales, divisa_comercio, numero_operacion, codigo_razon, mas_datos_adicionales, importe_original, signo_original, divisa_original, incluso_mas_datos_adicionales, fila_completa)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (cabecera_fichero_id,tipo_registro, fecha_valoracion_abono, numero_remesa, numero_factura_operacion, oficina_remesa, tarjeta, clase_tarjeta, modalidad_pago, entidad_tarjeta_emisora, fecha_operacion, hora_operacion, numero_autorizacion, tipo_operacion, captura_operacion, importe_operacion, signo_operacion, tasa_descuento, importe_descuento, signo_descuento, importe_liquido, signo_liquido, numero_tpv, arn, tasa_intercambio, gastos, datos_adicionales, divisa_comercio, numero_operacion, codigo_razon, mas_datos_adicionales, importe_original, signo_original, divisa_original, incluso_mas_datos_adicionales, fila_completa)
    cursor.execute(query, valores)


#Función para insertar datos cola comercio en la DB
def insertar_cola_comercio(cursor, cabecera_fichero_id, tipo_registro, datos_adicionales, numeros_operaciones_comercio, importe_total, signo, mas_datos_adicionales, fila_completa):
    #cursor = conexion.cursor()

    query = """
    INSERT INTO sabadell_cola_comercio (cabecera_fichero_id, tipo_registro, datos_adicionales, numeros_operaciones_comercio, importe_total, signo, mas_datos_adicionales, fila_completa)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (cabecera_fichero_id, tipo_registro, datos_adicionales, numeros_operaciones_comercio, importe_total, signo, mas_datos_adicionales, fila_completa)
    cursor.execute(query, valores)

#Función para insertar datos cola fichero en la DB
def insertar_cola_fichero(cursor, cabecera_fichero_id, tipo_registro, numero_comercios, datos_adicionales, numero_operaciones, importe_total, signo, mas_datos_adicionales, fila_completa):
    #cursor = conexion.cursor()

    query = """
    INSERT INTO sabadell_cola_fichero (cabecera_fichero_id, tipo_registro, numero_comercios, datos_adicionales, numero_operaciones, importe_total, signo, mas_datos_adicionales, fila_completa)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (cabecera_fichero_id, tipo_registro, numero_comercios, datos_adicionales, numero_operaciones, importe_total, signo, mas_datos_adicionales, fila_completa)
    cursor.execute(query, valores)