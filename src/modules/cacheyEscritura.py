import os
import pickle

def cargar_cache(ruta):
    # Deserializar y cargar los objetos de la lista de vuelos desde un archivo
    if os.path.exists(ruta):
        with open(ruta, 'rb') as archivo:
            return pickle.load(archivo)
    return None

def guardar_cache(ruta, vuelos):
    # Serializar y guardar los objetos de la lista de vuelos en un archivo
    with open(ruta, 'wb') as archivo:
        pickle.dump(vuelos, archivo)