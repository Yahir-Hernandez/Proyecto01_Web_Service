from datetime import datetime
from iatas import iatasC
from prediccion import predicc as pc
import os
import pandas as pd
import requests
import json

#Metodo para solicitar el clima de lugar que se da como parametro
def weather(lugar=""):
    key = "bafa68a647e077182f2e167abc8648dd"
    lat, lon = obtener_coordenadas(lugar) #valor la latitud y longitud del lugar
    url = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={key}"
    rp = requests.get(url) 
    
    # status_code sera igual a 200 si la solicitud fue recibida, entendida y procesada con éxito.
    if rp.status_code == 200:
        data = rp.json()
        
    carpeta_destino = os.path.join(os.path.dirname(__file__), '../cache') #definir una carpeta donde gaurdar los objetos
    nombre_archivo= f'climas.json' 
    ruta = os.path.join(carpeta_destino, nombre_archivo)

    with open(ruta, 'w') as archivo:
        json.dump(data, archivo)


def obtener_coordenadas(lugar=""):
    # Coordenadas por defecto: Aeropuerto Internacional de la Ciudad de México
    coordenadas_default = (19.4363, -99.0721)
    
    #Si el lugar es igual a "" entonces devolvera el la latitud y longitud del 
    #aeropuerto internacional de la Ciudad de México
    if lugar == "":
        return coordenadas_default

    # Construir la ruta al archivo CSV
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/data/dataset.csv'))
    
    # Leer el archivo CSV en un DataFrame
    try: 
        df = pd.read_csv(file_path)
    except Exception:
        return None

    # Obtener el código IATA del lugar especificado
    Iata = iatasC(lugar)
    
    # Buscar en las columnas 'origin' y 'destination'
    for columna in ["origin", "destination"]:
        busca = df[df[columna] == Iata]
        if not busca.empty:
            lat = busca[f"{columna}_latitude"].values[0]
            lon = busca[f"{columna}_longitude"].values[0]
            return lat, lon
    
    # Si no se encuentra el lugar, devolver None
    return None

lugar = input("ingresa el lugar: ")
latitud, longitud = obtener_coordenadas(lugar)
print(latitud)
print(longitud)

print(weather(lugar))