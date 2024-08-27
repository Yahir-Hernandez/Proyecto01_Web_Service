import json
import os
import pickle

def cargar_cache(ruta):
    # Deserializar y cargar los objetos de la lista de vuelos desde un archivo
    if os.path.exists(ruta):
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    return None

def guardar_cache(ruta, archivos):
    # Cargar los vuelos existentes desde el archivo si existe
    arch_existentes = cargar_cache(ruta)

    if arch_existentes: # Agregar los nuevos vuelos a la lista existente

        arch_existentes.extend(archivos)
    else:
        arch_existentes = archivos # Si no existen vuelos previos, usar solo los nuevos

    # Serializar y guardar la lista actualizada de vuelos en un archivo
    with open(ruta, 'w') as archivo:
        json.dump(arch_existentes, archivo, indent=4)

    
    

  
