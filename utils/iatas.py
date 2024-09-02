
import pandas as pd
import os
import sys


# Añadir el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.predicc import predicc

#Regresa el codigo IATA de la ciudad introducida
def iatasC(ciudad):
   
    # Construir la ruta al archivo JSON
    archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/IATAS.csv'))
    
    #LEE el pdf de pandas y lo regresa en un data frame
    try: 
        df = pd.read_csv(archivo)
    except Exception:
        return None
    
     # Formatear la entrada en modo capitalizado
    ct = predicc(ciudad.title())
    
    #Busca en la columna ciudad de "IATAS.csv" la conicidencia con la ciudad parametro
    ciudad = df[df["Ciudad"] == ct]
    
    #convierte el Df en una lista de un solo string
    iata_code = ciudad["IATA"].values 
    
    if len(iata_code) == 0:
        return "No regreso nada"
    
    #Devuelve el valor del string
    return iata_code[0]


