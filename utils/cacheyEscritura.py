import json
import os
import sys


def cargar_cache(ruta):
    # Deserializar y cargar los objetos de la lista de vuelos desde un archivo
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
    arch_existentes = cargar_cache(ruta)

    if arch_existentes: 

        arch_existentes.extend(archivos)
    else:
        arch_existentes = archivos # Si no existen vuelos previos, usar solo los nuevos

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


def carpetaCache():
    """
    Verifica si la carpeta 'cache' existe en el sistema de archivos y la crea si es necesario.
    Además, agrega la ruta de la carpeta al sys.path si aún no está presente.

    Args:
        None

    Returns:
        None
    """
    # Definir la ruta de la carpeta 'cache' relativa al archivo actual
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../cache'))

    # Verificar si la ruta está en el sys.path, si no, agregarla
    if file_path not in sys.path:
        sys.path.append(file_path)

    # Crear la carpeta si no existe
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    
    

  
