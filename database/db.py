import os 
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


#Creamos función para conectar a la DB
def conectar_db():
    try:
        return mysql.connector.connect(
            host = os.getenv('DB_HOST'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            database = os.getenv('DB_NAME'),
        )
    except Exception as error:
        print("Error conexión mysql. ", error)

## FUNCIONES TRANSACCIÓN ####

#Función para iniciar la transacción
def start_transaction(conexion):
        conexion.start_transaction()

#Función confirmar transacción
def commit_transaction(conexion):
    conexion.commit()

#Función revertir transacción en caso de error
def rollback_transaction(conexion):
    conexion.rollback()