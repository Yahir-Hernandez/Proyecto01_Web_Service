import json
import os

def cargar_cache(ruta):
    # Deserializar y cargar los objetos de la lista de vuelos desde un archivo
    if os.path.exists(ruta):
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    return None

def guardar_cache(ruta, archivos):
    
    arch_existentes = cargar_cache(ruta)

    if arch_existentes: 

        arch_existentes.extend(archivos)
    else:
        arch_existentes = archivos # Si no existen vuelos previos, usar solo los nuevos

    with open(ruta, 'w') as archivo:
        json.dump(arch_existentes, archivo, indent=4)

    
    

  
