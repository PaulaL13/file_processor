


## FUNCIONES PARA FORMATEAR DIFERENTES DATOS ##

def convertir_format_fecha(fecha):
    return f"{fecha[6:]}-{fecha[3:5]}-{fecha[:2]}"

def validar_decimal(valor):
    #Eliminamos espacios en blanco
    valor = valor.strip()
    if valor == '':
        #Si esta vacío, devolvemos un None
        return None 
    try: 
        return float(valor)/100
    except ValueError:
        return None