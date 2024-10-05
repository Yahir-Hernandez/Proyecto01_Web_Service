import os
import pandas as pd
import requests
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
from utils.horasyTiempo import hoy, timestamp, ayer, convertDT_a_CST, formato_dia_mes, formato_hora_minuto
from utils.iatas import iatasC
from utils.cacheyEscritura import cargar_cache, guardar_cache
from utils.predicc import predicc as pc
from utils.traductor import traducir_main

def weather(ciudad):
    
    if not ciudad or ciudad == "":
        raise Exception("Por favor selecciona un lugar válido para solicitar el clima.")

    carpeta_destino = os.path.join(os.path.dirname(__file__), '../utils/cache') 
    nombre_archivo= f'climas_{iatasC(ciudad)}.json' 

    ruta = os.path.join(carpeta_destino, nombre_archivo)

    climas = verificaEnCacheClima(ruta, ciudad)

    return climas

"""
    Obtiene el clima de un lugar específico, verificando primero en el caché 
    y solicitando datos de la API si no se encuentran coincidencias.

    Args:
        lugar (str): Nombre del lugar para solicitar el clima.

    Raises:
        Exception: Si no se proporciona un lugar válido.

    Returns:
        list: Lista de datos climáticos correspondientes al lugar solicitado.
""" 
def solicitarAPIClima(lugar):

    load_dotenv()
    
    key = os.getenv('WEATHER_KEY')
    lat, lon = obtener_coordenadas(lugar) 
    url = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={key}&units=metric&lang=es"
    rp = requests.get(url) 
    
    if rp.status_code != 200:
        raise Exception(f"Error en la solicitud de la API: {rp.status_code}")
    
    return rp.json()
"""
    Solicita el clima actual de una ciudad a través de la API de OpenWeather.

    Args:
        lugar (str): Nombre del lugar para el que se desea obtener el clima.

    Raises:
        Exception: Si ocurre un error en la solicitud a la API.

    Returns:
        dict: Respuesta en formato JSON con los datos climáticos del lugar solicitado.
"""

def solicitarAPIClimaHistorico(lugar):

    load_dotenv()
    
    key = os.getenv('WEATHER_KEY')
    lat, lon = obtener_coordenadas(lugar) 
    start = timestamp(ayer())
    end = timestamp(hoy())
    url = f"https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&start={start}&end={end}&appid={key}&units=metric"
    rp = requests.get(url)

    if rp.status_code != 200:
        raise Exception(f"Error en la solicitud de la API: {rp.status_code}")

    return rp.json()
"""
    Solicita el clima histórico de una ciudad para las horas previas a la hora actual.

    Args:
        lugar (str): Nombre del lugar para solicitar el clima histórico.

    Raises:
        Exception: Si ocurre un error en la solicitud a la API.

    Returns:
        dict: Respuesta en formato JSON con los datos climáticos históricos del lugar solicitado.
"""
    
def verificaEnCacheClima(ruta, ciudad):

    data_cache = cargar_cache(ruta)

    if data_cache:
        return data_cache

    data = solicitarAPIClimaHistorico(ciudad)
    climas_creados = crear_clima(data, ciudad)
    guardar_cache(ruta, climas_creados)

    data2 = solicitarAPIClima(ciudad)
    climas_creados2 = crear_clima(data2, ciudad)
    guardar_cache(ruta, climas_creados2)

    return climas_creados + climas_creados2

"""
    Verifica si los datos climáticos de una ciudad están almacenados en el caché.

    Args:
        ruta (str): Ruta del archivo de caché.
        ciudad (str): Nombre de la ciudad para buscar los datos climáticos en la caché.

    Returns:
        list: Lista de climas encontrados en la caché o solicitados a la API.
"""

def obtener_coordenadas(lugar):

    if not lugar or lugar == "":
        raise Exception("Por favor, selecciona un lugar válido para las coordenadas")
    
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../static/dataset.csv'))
    
    try: 
        df = pd.read_csv(file_path)
    except:
        raise Exception("No se pudo leer o no existe el archivo SCV dataset.")

    Iata = iatasC(lugar)

    for columna in ["origin", "destination"]:
        busca = df[df[columna] == Iata]
        if not busca.empty:
            lat = busca[f"{columna}_latitude"].values[0]
            lon = busca[f"{columna}_longitude"].values[0]
            return lat, lon
    return None

"""
    Obtiene las coordenadas (latitud y longitud) de un lugar a partir de un archivo CSV.

    Args:
        lugar (str): Nombre del lugar o código IATA.

    Raises:
        Exception: Si no se proporciona un lugar válido o no se puede leer el archivo CSV.

    Returns:
        tuple: Coordenadas (latitud, longitud) del lugar solicitado.
"""

def buscar_clima(clima_data, hora):

    for clima in clima_data:
        if clima['Fecha y hora']==hora:
            return clima
    return None

"""
    Busca datos climáticos en una lista de datos climáticos basándose en la ciudad y la hora.

    Args:
        clima_data (list): Lista de diccionarios con los datos climáticos.
        ciudad (str): Nombre de la ciudad para la cual se desea encontrar el clima.
        hora (str): Hora específica en formato 'YYYY-MM-DD HH:MM:SS' para buscar el clima.

    Returns:
        dict or None: Diccionario con los datos climáticos si se encuentra una coincidencia,
                      de lo contrario, retorna None.
"""


def crear_clima(json_data, ciudad):
    climas = []
    
    for clima_data in json_data.get('list', []):
        
        clima = {
            "Ciudad": ciudad,
            "Clima": clima_data.get('weather')[0].get('main'),
            "Descripcion": traducir_main(clima_data.get('weather')[0].get('id')),
            "Temperatura": clima_data.get('main').get('temp'),
            "Nubosidad": clima_data.get('clouds').get('all'),
            "Presion atmosferica": clima_data.get('main').get('pressure'),
            "Temperatura minima": clima_data.get('main').get('temp_min'),
            "Temperatura maxima": clima_data.get('main').get('temp_max'),
            "Velocidad del viento": clima_data.get('wind').get('speed'),
            "Direccion del viento": clima_data.get('wind').get('deg'),
            "Fecha y hora": convertDT_a_CST(clima_data.get('dt')),
            "Fecha simplificada": formato_dia_mes(convertDT_a_CST(clima_data.get('dt'))),
            "Hora simplificada": formato_hora_minuto(convertDT_a_CST(clima_data.get('dt'))),
            "Humedad": clima_data.get('main').get('humidity'),
            "Visibilidad": clima_data.get('visibility'),
            "icono": clima_data.get('weather')[0].get("icon") ,
            "Termica": clima_data.get('main').get("feels_like"),
        }
        climas.append(clima)
    
    return climas
"""
    Crea una lista de diccionarios que representan los datos climáticos de una ciudad a partir
    de los datos JSON obtenidos de la API.

    Args:
        json_data (dict): Datos JSON devueltos por la API de OpenWeather.
        ciudad (str): Nombre de la ciudad para la que se generarán los datos climáticos.

    Returns:
        list: Lista de diccionarios, donde cada uno contiene los detalles climáticos de un momento específico.
"""
