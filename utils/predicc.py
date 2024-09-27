from fuzzywuzzy import process, fuzz
import pandas as pd
import os
import  sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Módulo de predicción para la entrada de los usuarios
# Busca los resultados de entradas de usuario erróneas
#Regresa la mejor prediccion para la ciudad
def predicc(entrada):
    
    # Construir la ruta al archivo CSV
    archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), '../static/IATAS.csv'))
    
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

def porcentaje(palabra):
    '''
    Compara una palabra con un percentaje de la lista de ciudad registradas en IATAS.CSV ciudad
    @param palabra: elemento que se compara
    @return: porcentaje de parecido
    '''
    # Construir la ruta al archivo CSV
    archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), '../static/IATAS.csv'))

    # Leer el archivo CSV en un DataFrame
    try:
        df = pd.read_csv(archivo)
    except Exception:
        raise Exception("No se pudo leer o no existe el archivo CSV IATAS.")

    # Capitalizar la palabra
    ct = palabra.title()

    # Obtener los nombres de las ciudades
    nombres = df['Ciudad'].values

    # Almacenar los resultados en una lista de tuplas (ciudad, porcentaje)
    resultados = []

    # Calcular el porcentaje de similitud con cada ciudad
    for nombre in nombres:
        porcentaje_similitud = fuzz.ratio(ct, nombre)
        resultados.append((nombre, porcentaje_similitud))

    # Devolver los resultados ordenados por porcentaje de similitud (de mayor a menor)
    resultados_ordenados = sorted(resultados, key=lambda x: x[1], reverse=True)

    return resultados_ordenados