from datetime import datetime, timedelta
import json
import os
import sys
from utils.horasyTiempo import hoy

def cargar_cache(ruta):
    if os.path.exists(ruta):
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    return None
"""
    Deserializa y carga los objetos de la lista de vuelos desde un archivo JSON.

    Args:
        ruta (str): La ruta del archivo JSON desde el cual se cargarán los datos.

    Returns:
        list or None: Devuelve una lista de objetos si el archivo existe y fue cargado exitosamente.
                      Devuelve None si el archivo no existe.
"""

def guardar_cache(ruta, archivos):
    carpetaCache()
    guardaFecha()

    arch_existentes = cargar_cache(ruta)

    if arch_existentes: 
        archivos_nuevos = [archivo for archivo in archivos if archivo not in arch_existentes]
        arch_existentes.extend(archivos_nuevos)
    else:
        arch_existentes = archivos 

    with open(ruta, 'w') as archivo:
        json.dump(arch_existentes, archivo, indent=4)

"""
    Guarda los nuevos archivos en el caché, extendiendo la lista existente si ya hay datos previos.

    Args:
        ruta (str): La ruta del archivo JSON donde se guardarán los datos.
        archivos (list): Una lista de objetos que se desea agregar o guardar en el archivo de caché.

    Returns:
        None
"""

def guardaIATAS(iatas):
    ruta = os.path.join(os.path.dirname(__file__), '../utils/cache')
    archivo_txt = os.path.join(ruta, 'ejemplo_tickets.txt')

    if not os.path.exists(ruta):
        os.makedirs(ruta)
        
    with open(archivo_txt, 'w') as file:
        for iata in iatas:
            file.write(iata + '\n')

"""
    Guarda una lista de códigos IATA en un archivo de texto dentro de la carpeta 'cache'. 
    Si la carpeta no existe, la crea antes de escribir el archivo.

    Args:
        iatas (list): Una lista de códigos IATA (cadenas) que se desea guardar en el archivo.

    Returns:
        None

    Ejemplo:
        Si se pasa una lista de códigos IATA como ["MEX", "LAX", "JFK"], la función creará 
        (o sobrescribirá) el archivo 'ejemplo_tickets.txt' en la carpeta 'cache' y escribirá 
        cada código IATA en una nueva línea del archivo.

    Excepciones:
        - Si no se tienen permisos para crear el directorio o escribir el archivo, se lanzará 
          un `OSError` o `PermissionError`, lo que requeriría que el usuario verifique los 
          permisos de escritura en el sistema de archivos.

"""

def guardaFecha():

    ruta = os.path.join(os.path.dirname(__file__), '../utils/cache/fecha.txt')

    if not os.path.exists(ruta):
        with open(ruta, 'w') as archivo:
            archivo.write(hoy())

"""
    Guarda la fecha actual en un archivo de texto llamado 'fecha.txt' dentro de la carpeta 'cache'.
    Si la carpeta o el archivo no existen, la función los creará antes de escribir la fecha.

    Args:
        None

    Returns:
        None

    Ejemplo:
        La función obtiene la fecha actual llamando a la función `hoy()` y la guarda en el archivo 
        'fecha.txt' en la carpeta 'cache'. Si la carpeta 'cache' no existe, se creará automáticamente.

    Excepciones:
        - Si no se puede crear la carpeta o el archivo debido a restricciones de permisos, se lanzará 
          un `OSError` o `PermissionError`, indicando que el sistema no puede completar la operación.
"""


def carpetaCache():
   
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils/cache'))

    if file_path not in sys.path:
        sys.path.append(file_path)

    if not os.path.exists(file_path):
        os.makedirs(file_path)

"""
    Verifica si la carpeta 'cache' existe en el sistema de archivos y la crea si es necesario.
    Además, agrega la ruta de la carpeta al sys.path si aún no está presente.

    Args:
        None

    Returns:
        None
"""
 
def decide_SiBorrarCache():

    ruta = os.path.join(os.path.dirname(__file__), '../utils/cache/fecha.txt')
    cache = os.path.join(os.path.dirname(__file__), '../utils/cache')
    actual = datetime.strptime(hoy() , '%Y-%m-%d %H:%M:%S')

    if os.path.exists(ruta):

        with open(ruta, 'r') as archivo:
            fecha = datetime.strptime(archivo.read().strip(), '%Y-%m-%d %H:%M:%S')

        diferencia = actual - fecha

        if diferencia > timedelta(hours=20):
            eliminarTickets(cache)
            eliminarClimas(cache)
            os.remove(ruta)

"""
    Verifica si han pasado más de 20 horas desde la última vez que se guardó la fecha en el archivo de caché.
    Si es así, elimina los archivos relacionados con climas y tickets en la carpeta 'cache' y borra el archivo
    que contiene la fecha.

    Args:
        None

    Returns:
        None
"""

def eliminarClimas(ruta):

    for file in os.listdir(ruta):
        if file.startswith('climas_'):
            os.remove(os.path.join(ruta, file))

"""
    Elimina todos los archivos en la carpeta especificada que comiencen con el prefijo 'climas_'.
    Esto permite gestionar la limpieza de archivos de caché relacionados con el clima.

    Args:
        ruta (str): La ruta a la carpeta donde se encuentran los archivos de caché.

    Returns:
        None
"""


def eliminarTickets(ruta):

    for file in os.listdir(ruta):
        if file.startswith('tickets_'):
            os.remove(os.path.join(ruta, file))

"""
    Elimina todos los archivos en la carpeta especificada que comiencen con el prefijo 'tickets_'.
    Esto permite gestionar la limpieza de archivos de caché relacionados con los tickets de vuelo.

    Args:
        ruta (str): La ruta a la carpeta donde se encuentran los archivos de caché.

    Returns:
        None
"""
