# Procesador de Ficheros de Operaciones e Inserción en MySQL

Este repositorio contiene un programa en Python que procesa ficheros de operaciones de comercios y los inserta en una base de datos MySQL. Los ficheros procesados son proporcionados por Banco Sabadell y contienen información sobre la operativa de tarjetas de crédito y débito.

## Descripción del Proyecto

El programa está diseñado para automatizar la carga de datos de los siguientes tipos de ficheros proporcionados diariamente por Banco Sabadell:

1. **Fichero de Operaciones**: Contiene información de las operaciones procesadas y liquidadas.
2. **Fichero de Retrocesiones (Chargebacks)**: Incluye retrocesiones solicitadas por los titulares de las tarjetas.
3. **Fichero de Fraude Confirmado**: Reporta operaciones fraudulentas que no fueron realizadas ni autorizadas por los titulares.
4. **Fichero de Peticiones de Documentación**: Solicita justificantes de las transacciones para verificación.

El objetivo del proyecto es facilitar la gestión de la información recibida, permitiendo a los usuarios almacenar estos datos en una base de datos para análisis y gestión interna.

Esta primera fase se ha desarrollado del **Fichero de Operaciones**.

## Características

- **Procesamiento Automático**: Lee los ficheros en formatos predefinidos y extrae los datos relevantes.
- **Inserción en MySQL**: Inserta la información extraída en tablas específicas de una base de datos MySQL.
- **Verificación de Consistencia**: Asegura que todas las líneas de los ficheros sean procesadas correctamente y evita inserciones duplicadas.

## Estructura de los Ficheros

Cada fichero tiene una estructura particular que debe ser interpretada para su correcta inserción en la base de datos:

- **Cabecera de Fichero**: Contiene metadatos generales como fecha de proceso, rango de fechas de las operaciones y número de contrato del comercio.
- **Registro de Operación**: Incluye detalles de cada operación, como fecha, importe, tipo de operación, número de tarjeta, etc.
- **Cola de Comercio y Cola de Fichero**: Proporcionan información agregada sobre el número de operaciones y su importe total.

## Requisitos

- **Python 3.8+**
- **MySQL Server**
- Librerías de Python:
  - `mysql-connector-python` para la conexión a la base de datos MySQL.
  - `python-dotenv` para manejar variables de entorno.

Puedes instalar las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

## Configuración

Para configurar la conexión a la base de datos, se debe crear un archivo `.env` con las siguientes variables:

```env
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=nombre_base_datos
```

Debes indicar donde la ruta donde están los ficheros .TXT.
```
RUTA = '/home/paula_leal/inbound_sabadell/TARJETA'
```
## Uso

1. Coloca los ficheros a procesar en el directorio de entrada especificado.
2. Ejecuta el script principal:

```bash
python procesar_ficheros.py
```

El script leerá cada fichero, procesará sus registros y los insertará en la base de datos.


## Estructura de la Base de Datos

El programa utiliza las siguientes tablas en MySQL para almacenar los datos:

- **sabadell\_cabecera\_fichero**: Almacena la información general del fichero.
- **sabadell\_cabecera\_remesa**: Almacena datos específicos de cada remesa.
- **cola\_comercio**: Contiene datos agregados sobre las operaciones del comercio.
- **cola\_fichero**: Almacena información agregada de todo el fichero.
- **sabadell\_registro\_operacion**: Guarda los detalles de cada operación realizada.

Ejecuta el fichero create_tables.sql en tu cliente mysql para crear las tablas y campos correspondientes.

## Ejemplo de Uso

Un ejemplo de fichero de operaciones contiene registros con los siguientes campos:

- **Tipo de Registro**: Indica el tipo de registro (cabecera, operación, etc.).
- **Fecha de Proceso**: Fecha de liquidación de las operaciones.
- **Valor**: Fecha de valoración del abono.
- **Importe de Operación**: Cantidad nominal de la operación.


## Licencia

Este programa es de código abierto y puede ser utilizado, modificado y distribuido por cualquier persona, siempre y cuando se mencione al autor original en cualquier redistribución o versión derivada.

El código está en una fase inicial de desarrollo y aún falta implementar muchas mejoras. Si encuentras errores o realizas mejoras, ¡no dudes en contribuir con issue o pull request!

**Autor:** Paula Leal
