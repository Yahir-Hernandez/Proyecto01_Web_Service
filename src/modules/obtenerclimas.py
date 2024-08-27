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

    lugar = lugar.replace(" ", "")
    
    if not lugar or lugar == "":
        raise Exception("Por favor selecciona un lugar válido.")
    
    lugar = pc(lugar)
    
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
            if clima['Ciudad'] == ciudad:
                climas_encontrados.append(clima)

        # Si se encontraron climas, devolverlos
        if climas_encontrados:
            print("Coincidencias encontradas en caché.")
            return climas_encontrados

    # Si no hay coincidencias en el caché, solicitar nuevos datos a la API
    print("Clima no encontrado en caché. Solicitando datos a la API.")
    data = solictarAPIClima(ciudad)
    climas_creados = crear_clima(data, ciudad)
    guardar_cache(ruta, climas_creados)

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

def crear_clima(json_data, ciudad):
    climas = []
    
    for clima_data in json_data.get('list', []):
        #Usar get en lugar de acceder directamente a las claves y listas.
        #Evitar excepciones si una clave no está presente en el diccionario.
        clima = {
            "Ciudad": ciudad,
            "Clima": clima_data.get('weather')[0].get('main'),
            "Descripcion": clima_data.get('weather')[0].get('description'),
            "Temperatura": clima_data.get('main').get('temp'),
            "Nubosidad": clima_data.get('clouds').get('all'),
            "Presión a nivel del mar": clima_data.get('main').get('sea_level'),
            "Presión a nivel del suelo": clima_data.get('main').get('grnd_level'),
            "Presión atmosférica": clima_data.get('main').get('pressure'),
            "Temperatura minima": clima_data.get('main').get('temp_min'),
            "Temperatura maxima": clima_data.get('main').get('temp_max'),
            "Velocidad del viento": clima_data.get('wind').get('speed'),
            "Dirección del viento": clima_data.get('wind').get('deg'),
            "Ráfagas del viento": clima_data.get('wind').get('gust'),
            "Fecha y hora": clima_data.get('dt_txt'),
            "Humedad": clima_data.get('main').get('humidity'),
            "Visibilidad": clima_data.get('visibility'),
        }
        climas.append(clima)
    
    return climas

