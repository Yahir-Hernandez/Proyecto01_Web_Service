import json
import os
import sys


def cargar_cache(ruta):
    # Deserializar y cargar los objetos de la lista de vuelos desde un archivo
    if os.path.exists(ruta):
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    return None

def guardar_cache(ruta, archivos):
    carpetaCache()
    arch_existentes = cargar_cache(ruta)

    if arch_existentes: 

        arch_existentes.extend(archivos)
    else:
        arch_existentes = archivos # Si no existen vuelos previos, usar solo los nuevos

    with open(ruta, 'w') as archivo:
        json.dump(arch_existentes, archivo, indent=4)


def carpetaCache():
    '''
    Revisa si existe la carpeta cache, si no, la crea
    '''
    # Definir la ruta de la carpeta 'cache' relativa al archivo actual
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../cache'))

    # Verificar si la ruta está en el sys.path, si no, agregarla
    if file_path not in sys.path:
        sys.path.append(file_path)

    # Crear la carpeta si no existe
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    
    

  
