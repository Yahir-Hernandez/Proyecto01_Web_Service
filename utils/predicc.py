from fuzzywuzzy import process, fuzz
import pandas as pd
import os
import  sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def predicc(entrada):
    
    archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), '../static/IATAS.csv'))
    
    try: 
        df = pd.read_csv(archivo)
    except Exception:
        raise Exception ("No se pudo leer o no existe el archivo CSV IATAS.")

    iata = df[df["IATA"] == entrada.upper()]
    if not iata.empty:
        return iata["Ciudad"].values[0]
    
    ct = entrada.title()
    
    nombres = df['Ciudad'].values

    coincidencias = process.extractOne(ct, nombres, score_cutoff=70)

    if coincidencias:

        return coincidencias[0]
    else:

        raise Exception("No se encontraron coincidencias para esa ciudad.")
    
"""
    Predice y corrige el nombre de una ciudad basada en una entrada dada, utilizando coincidencias
    aproximadas con los datos del archivo IATAS.csv.

    Args:
        entrada (str): La ciudad o código IATA proporcionado por el usuario.

    Returns:
        str: El nombre corregido de la ciudad si se encuentra una coincidencia.

    Raises:
        Exception: Si no se puede leer el archivo CSV o si no se encuentran coincidencias.
"""

def porcentaje(palabra):

    archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), '../static/IATAS.csv'))

    try:
        df = pd.read_csv(archivo)
    except Exception:
        raise Exception("No se pudo leer o no existe el archivo CSV IATAS.")

    ct = palabra.title()

    nombres = df['Ciudad'].values

    resultados = []

    for nombre in nombres:
        porcentaje_similitud = fuzz.ratio(ct, nombre)
        resultados.append((nombre, porcentaje_similitud))

    resultados_ordenados = sorted(resultados, key=lambda x: x[1], reverse=True)

    return resultados_ordenados

"""
        Calcula el porcentaje de similitud entre una palabra dada y los nombres de ciudades del archivo IATAS.csv,
        ordenando los resultados por mayor similitud.

        Args:
            palabra (str): La palabra o ciudad proporcionada por el usuario.

        Returns:
            list: Una lista de tuplas con los nombres de las ciudades y su porcentaje de similitud,
            ordenada de mayor a menor.
"""