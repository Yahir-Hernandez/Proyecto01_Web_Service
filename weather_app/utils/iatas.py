
import pandas as pd
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.predicc import predicc


def iatasC(ciudad):
   
    archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), '../static/IATAS.csv'))
    
    try: 
        df = pd.read_csv(archivo)
    except Exception:
        raise Exception("No se pudo leer o no existe el archivo CSV IATAS.")
    
    ct = predicc(ciudad.title())
    
    ciudad = df[df["Ciudad"] == ct]
    
    iata_code = ciudad["IATA"].values 
    
    if len(iata_code) == 0:
        raise Exception("No se encontró el IATA")
    
    return iata_code[0]

"""
    Obtiene el código IATA correspondiente a una ciudad dada.

    Esta función lee un archivo CSV que contiene las ciudades y sus códigos IATA. 
    Primero, intenta cargar el archivo, y si no se puede leer, lanza una excepción con un mensaje específico. 
    Luego, utiliza la función `predicc` para corregir el nombre de la ciudad y busca en el DataFrame el código IATA. 
    Si no encuentra un código IATA para la ciudad, se lanza otra excepción.

    Args:
        ciudad (str): Nombre de la ciudad para la cual se desea obtener el código IATA.

    Raises:
        Exception: Si el archivo CSV no se puede leer o no existe, 
                   o si no se encuentra el código IATA correspondiente a la ciudad.

    Returns:
        str: El código IATA de la ciudad especificada.

    Examples:
        >>> iatasC("Tepic")
        "TPQ"
"""


