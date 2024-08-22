from fuzzywuzzy import process
import pandas as pd
import os

# Módulo de predicción para la entrada de los usuarios
# Busca los resultados de entradas de usuario erróneas
#Regresa la mejor prediccion para la ciudad
def predicc(entrada=""):
    
    if entrada == "":
        return "Ciudad de México"
    
    #diccionario donde se alamacera el json cargado
    datos = {}
    
    
    # Construir la ruta al archivo JSON
    archivo = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/data/IATAS.csv'))
    
    # Manejo de errores al abrir el archivo
    #LEE el pdf de pandas y lo regresa en un data frame
    try: 
        df = pd.read_csv(archivo)
    except Exception:
        return None
    
    #genera un data frame de la fila de la IATA encontrada
    iata = df[df["IATA"] == entrada.upper()]
    if not iata.empty:
        res = iata["Ciudad"].values
        return res[0]
    
    # Formatear la entrada
    ct = entrada.title()
    
    #data frame de la columna ciudad
    ciudad = df['Ciudad']

    # Obtener los nombres de las ciudades
    nombres = ciudad.values

    # Buscar la mejor coincidencia
    coincidencias = process.extractOne(ct, nombres)

    if coincidencias:
        #Regresa la mejor coincidencia
        "Borra este print, solo es para pruebas" 
        print(f"Mejor coincidencia para '{ct}': {coincidencias[0]} con un puntaje de {coincidencias[1]}")
        return coincidencias[0]  # Retorna la mejor coincidencia para uso posterior
    else:
        #Regresa la mejor coicidencias
        "Borra este print, solo es para pruebas" 
        print(f"No se encontró una coincidencia para '{ct}'.")
        return None
    
if __name__ == "__main__":
    ci = input()
    predicc(ci)
