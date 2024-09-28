
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
    Busca y devuelve el código IATA de una ciudad dada.

    Args:
        ciudad (str): El nombre de la ciudad cuyo código IATA se desea obtener.

    Returns:
        str: El código IATA correspondiente a la ciudad.

    Raises:
        Exception: Si no se puede leer el archivo CSV o si no se encuentra un código IATA para la ciudad.
"""
