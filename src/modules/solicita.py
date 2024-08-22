from datetime import datetime
from iatas import iatasC
from prediccion import predicc as pc
import os
import pandas as pd
import requests
import json

def weather(lugar=""):
    key = "bafa68a647e077182f2e167abc8648dd"
    lat = lati(lugar)
    lon = long(lugar)
    url = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={key}"
    rp = requests.get(url)
    
    if rp.status_code == 200:
        data = rp.json()
        
        # Crear la ruta absoluta a la carpeta 'src/data'
        carpeta_destino = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/data'))
        nombre_archivo = f'clima_{pc(lugar)}.json'

        # Crear la carpeta si no existe
        os.makedirs(carpeta_destino, exist_ok=True)

        # Ruta completa del archivo JSON
        ruta_completa = os.path.join(carpeta_destino, nombre_archivo)

        # Guardar el JSON en un archivo
        with open(ruta_completa, "w") as archivo:
            json.dump(data, archivo, indent=4)
        
        print(f"Datos guardados en: {ruta_completa}")
    else:
        print(f"Error {rp.status_code}: {rp.json()}")
        return "No se pudo obtener el clima. Verifica el nombre de la ciudad."
    
    
def lati(lugar=""):
    
    if lugar == "":
        return 19.4363

    # Construir la ruta al archivo JSON
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/data/dataset.csv'))
    
    #LEE el pdf de pandas y lo regresa en un data frame
    try: 
        df = pd.read_csv(file_path)
    except Exception:
        return None
    
    Iata = iatasC(lugar)
    
    columna = "origin"
    busca = df[df[columna] == Iata]
    
    if busca.empty:
        columna = "destination"
        busca = df[df[columna] == Iata]
    
    lat = busca[f"{columna}_latitude"].values
    return lat[0]

def long(lugar=""):
    
    if lugar == "":
        return -99.0721
    
    # Construir la ruta al archivo JSON
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/data/dataset.csv'))
    
    #LEE el pdf de pandas y lo regresa en un data frame
    try: 
        df = pd.read_csv(file_path)
    except Exception:
        return None
    
    Iata = iatasC(lugar)
    
    columna = "origin"
    busca = df[df[columna] == Iata]
    
    if busca.empty:
        columna = "destination"
        busca = df[df[columna] == Iata]
    
    lat = busca[f"{columna}_longitude"].values
    return lat[0]

lugar = input("ingresa el lugar: ")
print(f"latitud: {lati(lugar)}")
print(f"longitud: {long(lugar)}")

weather(lugar)