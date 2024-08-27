import json
import os
import pickle

def cargar_cache(ruta):
    # Deserializar y cargar los objetos de la lista de vuelos desde un archivo
    if os.path.exists(ruta):
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    return None

def guardar_cache(ruta, vuelos):
    # Cargar los vuelos existentes desde el archivo si existe
    vuelos_existentes = cargar_cache(ruta)

    if vuelos_existentes: # Agregar los nuevos vuelos a la lista existente

        vuelos_existentes.extend(vuelos)
    else:
        vuelos_existentes = vuelos # Si no existen vuelos previos, usar solo los nuevos

    # Serializar y guardar la lista actualizada de vuelos en un archivo
    with open(ruta, 'w') as archivo:
        json.dump(vuelos_existentes, archivo, indent=4)

    
    

  
