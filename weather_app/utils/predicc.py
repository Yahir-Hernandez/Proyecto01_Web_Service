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

    coincidencias = process.extractOne(ct, nombres, score_cutoff=80)

    if coincidencias:
        return coincidencias[0]
    else:
        raise Exception("No se encontraron coincidencias para esa ciudad.")
    
"""
    Busca la ciudad correspondiente a un código IATA o intenta corregir el nombre de la ciudad ingresado.

    Esta función recibe una entrada que puede ser un código IATA o un nombre de ciudad,
    busca la ciudad correspondiente en un archivo CSV que contiene códigos IATA y nombres de ciudades. 
    Si se proporciona un código IATA, se devuelve el nombre de la ciudad correspondiente. 
    Si se proporciona un nombre de ciudad que no coincide exactamente, se utiliza una 
    coincidencia difusa para encontrar la ciudad más similar.

    Args:
        entrada (str): Un código IATA o el nombre de una ciudad.

    Raises:
        Exception: Lanza una excepción si el archivo CSV no se puede leer o si no se 
                   encuentra una coincidencia para la entrada proporcionada.

    Returns:
        str: El nombre de la ciudad correspondiente al código IATA o el nombre de 
             la ciudad más similar encontrada.
"""

def porcentaje(palabra):

    archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), '../static/IATAS.csv'))

    try:
        df = pd.read_csv(archivo)
    except Exception:
        raise Exception("No se pudo leer o no existe el archivo CSV IATAS.")

    iata = df[df["IATA"] == palabra.upper()]
    if not iata.empty:
        return [('E','75'),('R','75')]

    ct = palabra.title()

    nombres = df['Ciudad'].values

    resultados = []

    for nombre in nombres:
        porcentaje_similitud = fuzz.ratio(ct, nombre)
        resultados.append((nombre, porcentaje_similitud))

    resultados_ordenados = sorted(resultados, key=lambda x: x[1], reverse=True)

    return resultados_ordenados

"""
    Calcula el porcentaje de similitud entre una palabra y los nombres de ciudades en el archivo CSV.

    Esta función recibe una palabra y verifica si coincide con un código IATA en el archivo CSV.
    Si coincide, retorna un valor fijo para la similitud. De lo contrario, calcula el 
    porcentaje de similitud de la palabra con cada ciudad en el archivo y devuelve 
    una lista de tuplas con el nombre de la ciudad y su porcentaje de similitud.

    Args:
        palabra (str): Un código IATA o el nombre de una ciudad.

    Raises:
        Exception: Lanza una excepción si el archivo CSV no se puede leer.

    Returns:
        list: Una lista de tuplas donde cada tupla contiene el nombre de la ciudad y 
              el porcentaje de similitud.
"""


