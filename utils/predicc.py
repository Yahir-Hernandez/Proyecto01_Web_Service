from fuzzywuzzy import process
import pandas as pd
import os
import  sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Módulo de predicción para la entrada de los usuarios
# Busca los resultados de entradas de usuario erróneas
#Regresa la mejor prediccion para la ciudad
def predicc(entrada):
    
    # Construir la ruta al archivo CSV
    archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/IATAS.csv'))
    
    # Leer el archivo CSV en un DataFrame
    try: 
        df = pd.read_csv(archivo)
    except Exception:
        raise Exception ("No se pudo leer o no existe el archivo CSV IATAS.")

    # Buscar la ciudad por código IATA
    iata = df[df["IATA"] == entrada.upper()]
    if not iata.empty:
        return iata["Ciudad"].values[0]
    
    # Formatear la entrada para coincidencias
    ct = entrada.title()
    
    # Obtener los nombres de las ciudades
    nombres = df['Ciudad'].values

    # Buscar la mejor coincidencia
    coincidencias = process.extractOne(ct, nombres, score_cutoff=70)

    if coincidencias:
        # Retornar la mejor coincidencia
        return coincidencias[0]
    else:
        # No se encontró una coincidencia
        raise Exception("No se encontraron coincidencias para esa ciudad.")
