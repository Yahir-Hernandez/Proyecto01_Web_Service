from fuzzywuzzy import process
import pandas as pd
import os

# Módulo de predicción para la entrada de los usuarios
# Busca los resultados de entradas de usuario erróneas
#Regresa la mejor prediccion para la ciudad
def predicc(entrada=""):
    if entrada == "":
        return "Ciudad de México"
    
    # Construir la ruta al archivo CSV
    archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/data/IATAS.csv'))
    
    # Leer el archivo CSV en un DataFrame
    try: 
        df = pd.read_csv(archivo)
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")
        return None

    # Buscar la ciudad por código IATA
    iata = df[df["IATA"] == entrada.upper()]
    if not iata.empty:
        return iata["Ciudad"].values[0]
    
    # Formatear la entrada para coincidencias
    ct = entrada.title()
    
    # Obtener los nombres de las ciudades
    nombres = df['Ciudad'].values

    # Buscar la mejor coincidencia
    coincidencias = process.extractOne(ct, nombres)

    if coincidencias:
        # Retornar la mejor coincidencia
        return coincidencias[0]
    else:
        # No se encontró una coincidencia
        return None
    
if __name__ == "__main__":
    ci = input()
    print(predicc(ci))
