from datetime import datetime, timedelta
import json
import os
import sys
from horasyTiempo import hoy

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

def guardaFecha():

    ruta = os.path.join(os.path.dirname(__file__), '../utils/cache/fecha.txt')

    if not os.path.exists(ruta):
        with open(ruta, 'w') as archivo:
            archivo.write(hoy())


def carpetaCache():
    """
    Verifica si la carpeta 'cache' existe en el sistema de archivos y la crea si es necesario.
    Además, agrega la ruta de la carpeta al sys.path si aún no está presente.

    Args:
        None

    Returns:
        None
    """
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils/cache'))

    if file_path not in sys.path:
        sys.path.append(file_path)

    if not os.path.exists(file_path):
        os.makedirs(file_path)
    
    
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

def eliminarClimas(ruta):

    for file in os.listdir(ruta):
        if file.startswith('climas_'):
            os.remove(os.path.join(ruta, file))


def eliminarTickets(ruta):

    for file in os.listdir(ruta):
        if file.startswith('tickets_'):
            os.remove(os.path.join(ruta, file))


