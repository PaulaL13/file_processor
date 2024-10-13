import os
from datetime import datetime


## CARPETA LOGS ##
def crear_carpeta_logs():
    #fecha_actual = datetime.now().strftime("%d-%m-%Y")
    carpeta_log = os.path.join('log')
    #Verificamos si la carpeta existe, y si no, la creamos nosotros
    if not os.path.exists(carpeta_log):
        os.makedirs(carpeta_log)

    return carpeta_log


def registrar_logs(dataLogError):

    # Acceder a los valores del diccionario
    nombre_fichero = dataLogError["nombre_fichero"]
    total_lineas = dataLogError["total_lineas"]
    lineas_guardadas = dataLogError["lineas_guardadas"]
    error = dataLogError["error"]

    carpeta_log = crear_carpeta_logs()

    fecha_hora = datetime.now().strftime("%d-%m-%Y")

    archivo_log = os.path.join(carpeta_log, f"log_{fecha_hora}.txt")

    with open(archivo_log,'a') as log:
        log.write(f"Fecha del procesamiento: {fecha_hora}\n")
        log.write(f"Nombre del fichero: {nombre_fichero}\n")
        log.write(f"Número total de líneas en el fichero: {total_lineas}\n")
        log.write(f"Número de líneas procesadas: {lineas_guardadas}\n")
        if (len(error)>5):
            log.write(f"El error ocurrido es el siguiente: {error}\n")
        log.write("---------------------------------------------------------\n")

## funcion Enviar al log un error
def crearErrorLog(nombre_fichero, error):
    dataLogError = {
             "nombre_fichero": nombre_fichero,
             "total_lineas": 0,
             "lineas_guardadas": 0,
             "error": error
    }
    registrar_logs(dataLogError)
