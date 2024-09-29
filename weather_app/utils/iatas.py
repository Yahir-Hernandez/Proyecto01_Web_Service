
import pandas as pd
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.predicc import predicc


def iatasC(ciudad):
   
<<<<<<< HEAD:utils/iatas.py
    # Construir la ruta al archivo JSON
=======
>>>>>>> Said:weather_app/utils/iatas.py
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


