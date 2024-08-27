from datetime import datetime
from iatas import iatasC
from cacheyEscritura import cargar_cache
from cacheyEscritura import guardar_cache
from prediccion import predicc as pc
import os
import pandas as pd
import requests
import json

#Metodo para solicitar el clima de lugar que se da como parametro
def weather(lugar):

    carpeta_destino = os.path.join(os.path.dirname(__file__), '../cache') #definir una carpeta donde gaurdar los objetos
    nombre_archivo= f'climas_cache.json' 
    ruta = os.path.join(carpeta_destino, nombre_archivo)

    climas = verificaEnCacheClima(ruta, lugar)

    return print(climas)

def solictarAPIClima(lugar):

    key = "bafa68a647e077182f2e167abc8648dd"
    lat, lon = obtener_coordenadas(lugar) #valor la latitud y longitud del lugar
    url = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={key}&units=metric&lang=es"
    rp = requests.get(url) 
    
    # status_code sera igual a 200 si la solicitud fue recibida, entendida y procesada con éxito.
    if rp.status_code != 200:
        raise Exception(f"Error en la solicitud de la API: {rp.status_code}")
    
    return rp.json()

    
def verificaEnCacheClima(ruta, ciudad):

    # Cargar los datos de clima desde el archivo de caché si existe
    data_cache = cargar_cache(ruta)
    climas_encontrados = []

    if data_cache:
        print("Verificando coincidencias en caché...")

        # Buscar en la lista de climas los que coincidan con la ciudad proporcionada
        for clima in data_cache:
            if clima['city']['name'] == ciudad:
                climas_encontrados.append(clima)

        # Si se encontraron climas, devolverlos
        if climas_encontrados:
            print("Coincidencias encontradas en caché.")
            return climas_encontrados

    # Si no hay coincidencias en el caché, solicitar nuevos datos a la API
    print("Clima no encontrado en caché. Solicitando datos a la API.")
    data = solictarAPIClima(ciudad)
    #climas_creados = crear_clima(data)
    guardar_cache(ruta, data)

    return data


def obtener_coordenadas(lugar):

    if not lugar or lugar == "":
        raise Exception("Por favor, selecciona un lugar válido")
    
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
"""
def crear_clima(json_data):
    climas = []
    for clima_data in json_data:
        clima = {
            "Ciudad": clima_data['city']['name'],
            "Clima": clima_data['weather']['main'],
            "Descripcion": clima_data['weather']['description'],
            "Temperatura": clima_data['main']['temp'],
            "Nubosidad": clima_data['clouds']['all'],
            "Presión a nivel del mar": clima_data['main']['sea_level'],
            "Presión a nivel del suelo": clima_data['main']['grnd_level'],
            "Presión atmosférica": clima_data['main']['pressure'],
            "Temperatura minima": clima_data['main']['temp_min'],
            "Temperatura maxima": clima_data['main']['temp_max'],
            "Velocidad del viento": clima_data['wind']['speed'],
            "Dirección del viento": clima_data['wind']['deg'],
            "Ráfagas del viento": clima_data['wind']['gust'],
            "Fecha y hora": clima_data['dt_txt'],
            "Humedad": clima_data['main']['humidity'],
            "Visibilidad": clima_data['visibility'],
        }
        climas.append(clima)
    
    return climas
"""

weather("Monterrey")