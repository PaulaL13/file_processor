from utils.utils import convertir_format_fecha, validar_decimal
from ficheros.files_db import *


def procesar_cabecera_fichero(cursor, linea, cabecera_fichero_id, lineas_guardadas, nombre_fichero):
    #Dividimos la fila en diferentes bloques de datos (según nuestro fichero pdf)
    tipo_registro = linea[:2]
    fecha_proceso = linea[2:12]
    fecha_inicio = linea[12:22]
    fecha_final = linea[22:32]

    datos_adicionales = linea[32:220] #188 caracteres adicionales

    fila_completa = linea


    #Convertimos fechas del formato DD-MM-AAAA al formato AAAA-MM-DD
    fecha_proceso = convertir_format_fecha(fecha_proceso)
    fecha_inicio = convertir_format_fecha(fecha_inicio)
    fecha_final = convertir_format_fecha(fecha_final)

    lineas_guardadas.append(linea)

    cabecera_fichero_id = insertar_cabecera_fichero(cursor, tipo_registro, fecha_proceso, fecha_inicio, fecha_final, datos_adicionales, nombre_fichero, fila_completa)

    return cabecera_fichero_id

def procesar_cabecera_remesa(cursor, linea, cabecera_fichero_id, lineas_guardadas):

    tipo_registro = linea[:2]
    numero_contrato = linea[2:17] 
    numero_comercio = linea[17:27]
    cuenta_comercio = linea[27:47]
    oficina_gestora = linea[47:51]
    fecha_proceso = linea[51:61]
    fecha_inicio = linea[61:71]
    fecha_final = linea[71:81]

    datos_adicionales = linea[81:220] #139 caracteres adicionales

    fila_completa = linea

    #Convertimos fechas del formato DD-MM-AAAA al formato AAAA-MM-DD
    fecha_proceso = convertir_format_fecha(fecha_proceso)
    fecha_inicio = convertir_format_fecha(fecha_inicio)
    fecha_final = convertir_format_fecha(fecha_final)

    lineas_guardadas.append(linea)

    insertar_cabecera_remesa(cursor, cabecera_fichero_id, tipo_registro, numero_contrato, numero_comercio, cuenta_comercio, oficina_gestora, fecha_proceso, fecha_inicio, fecha_final, datos_adicionales, fila_completa)    

def procesar_registro_operacion(cursor, linea, cabecera_fichero_id, lineas_guardadas):

    tipo_registro = linea[:2]
    fecha_valoracion_abono = linea[2:12]
    numero_remesa = linea[12:22]
    numero_factura_operacion = linea[22:34]
    oficina_remesa = linea[34:38]
    tarjeta = linea[38:58]
    clase_tarjeta = linea[58:60]
    modalidad_pago = linea[60:61]
    entidad_tarjeta_emisora = linea[61:62]
    fecha_operacion = linea[62:72]
    hora_operacion = linea[72:78]
    numero_autorizacion = linea[78:84]
    tipo_operacion = linea[84:86]
    captura_operacion = linea[86:89]
    importe_operacion = validar_decimal(linea[89:100])
    signo_operacion = linea[100:101]
    tasa_descuento = validar_decimal(linea[101:106])
    importe_descuento = validar_decimal(linea[106:115])
    signo_descuento = linea[115:116]
    importe_liquido = validar_decimal(linea[116:129])
    signo_liquido = linea[129:130]
    numero_tpv = linea[130:143]
    arn = linea[143:166]
    tasa_intercambio = validar_decimal(linea[166:175])
    gastos = validar_decimal(linea[175:180])
    datos_adicionales = linea[180:181] ####
    divisa_comercio = linea[181:184]
    numero_operacion = linea[184:196]
    codigo_razon = linea[196:200]
    mas_datos_adicionales = linea[200:202] ###
    importe_original = validar_decimal(linea[202:215])
    signo_original = linea[215:216]
    divisa_original = linea[216:219]
    incluso_mas_datos_adicionales = linea[219:220] ##

    fila_completa = linea

    lineas_guardadas.append(linea)

    #Convertimos fechas del formato DD-MM-AAAA al formato AAAA-MM-DD
    fecha_valoracion_abono = convertir_format_fecha(fecha_valoracion_abono)
    fecha_operacion = convertir_format_fecha(fecha_operacion)

    insertar_registro_operacion(cursor, cabecera_fichero_id,tipo_registro, fecha_valoracion_abono, numero_remesa, numero_factura_operacion, oficina_remesa, tarjeta, clase_tarjeta, modalidad_pago, entidad_tarjeta_emisora, fecha_operacion, hora_operacion, numero_autorizacion, tipo_operacion, captura_operacion, importe_operacion, signo_operacion, tasa_descuento, importe_descuento, signo_descuento, importe_liquido, signo_liquido, numero_tpv, arn, tasa_intercambio, gastos, datos_adicionales, divisa_comercio, numero_operacion, codigo_razon, mas_datos_adicionales, importe_original, signo_original, divisa_original, incluso_mas_datos_adicionales, fila_completa)

def procesar_cola_comercio(cursor, linea, cabecera_fichero_id, lineas_guardadas):
    tipo_registro = linea[:2]
    datos_adicionales = linea[2:27]
    numeros_operaciones_comercio = linea[27:36]
    importe_total = validar_decimal(linea[36:49])
    signo = linea[49:50]
    mas_datos_adicionales = linea[50:220]
    fila_completa = linea

    lineas_guardadas.append(linea)

    insertar_cola_comercio(cursor, cabecera_fichero_id, tipo_registro, datos_adicionales, numeros_operaciones_comercio, importe_total, signo, mas_datos_adicionales, fila_completa)


def procesar_cola_fichero(cursor, linea, cabecera_fichero_id, lineas_guardadas):
    tipo_registro = linea[:2]
    numero_comercios = linea[2:11]
    datos_adicionales = linea[11:36] ###
    numero_operaciones = linea[36:45]
    importe_total = validar_decimal(linea[45:58])
    signo = linea[58:59]
    mas_datos_adicionales = linea[59:220] ###

    fila_completa = linea

    lineas_guardadas.append(linea)

    insertar_cola_fichero(cursor, cabecera_fichero_id, tipo_registro, numero_comercios, datos_adicionales, numero_operaciones, importe_total, signo, mas_datos_adicionales, fila_completa)
