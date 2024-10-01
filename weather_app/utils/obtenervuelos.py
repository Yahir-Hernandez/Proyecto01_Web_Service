import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
from utils.predicc import predicc
from utils.cacheyEscritura import cargar_cache, guardar_cache, guardaIATAS
from utils.horasyTiempo import formato_hora_minuto, formato_dia_mes, redondea_hora
import requests


#Si se ingresas origen en CDMX, se debe de ingresar destino
load_dotenv()
# Clave de acceso para la API
api_key = os.getenv('FLIGHT_KEY')
# Endpoint de la API para obtener información de vuelos
endpoint = 'http://api.aviationstack.com/v1/flights'
    

def obtener_vuelo(ticket):

    ticket = ticket.replace(" ", "")

    if not ticket or ticket=="":
        raise Exception("Por favor selecciona un formato de ticket válido.")
    
    carpeta_destino = os.path.join(os.path.dirname(__file__), '../utils/cache') #definir una carpeta donde gaurdar el json
    nombre_archivo= f'tickets_vuelo.json' 

    ruta = os.path.join(carpeta_destino, nombre_archivo) #Definir la ruta del archivo para guardar los objetos

    vuelo = verificaEnCachevuelo(ruta, ticket)

    return vuelo

"""
    Obtiene vuelos asociados a un código IATA específico, verificando primero en el caché.

    Args:
        iata (str): Código IATA de un aeropuerto.

    Raises:
        Exception: Si no se proporciona un IATA válido.

    Returns:
        list: Lista de vuelos encontrados o solicitados.
    """
def verificaEnCachevuelo(ruta, ticket):

    data_cache = cargar_cache(ruta)
    vuelos_encontrados = []

    if data_cache:

        for vuelo in data_cache:
            if vuelo['iata'] == ticket:
                vuelos_encontrados.append(vuelo)

        if vuelos_encontrados:
            return vuelos_encontrados

    # Si no hay coincidencias en el caché, solicitar nuevos datos a la API
    data_nueva = obtener_vuelosAPI(ticket)
    vuelo = crear_vuelos(data_nueva)
    guardar_cache(ruta, vuelo)

    return vuelo

"""
    Verifica si existen vuelos asociados a un código IATA en el caché y, si no, solicita los datos a la API.

    Args:
        ruta (str): La ruta del archivo de caché.
        iata (str): Código IATA a buscar.

    Returns:
        list: Lista de vuelos encontrados o solicitados.
    """

def obtenerIATAS():

    carpeta_destino = os.path.join(os.path.dirname(__file__), '../utils/cache') #definir una carpeta donde gaurdar el json
    nombre_archivo= f'tickets_vuelo.json' 

    ruta = os.path.join(carpeta_destino, nombre_archivo)

    vuelos = consulta_API()
    vuelo = crear_vuelos(vuelos)
    guardar_cache(ruta, vuelo)
    iatas = creaIATAS(vuelos)

    guardaIATAS(iatas)

def consulta_API():

    params = {
        'access_key': api_key,
        "limit" : 25,
        "dep_iata" : "MEX",
        "offset" : 0
    }

    apiresponse = requests.get(endpoint, params=params)

    if apiresponse.status_code != 200: 
        raise Exception(f"Error en la solicitud de la API: {apiresponse.status_code}")

    return apiresponse.json()

def creaIATAS(json_data):

    vuelos = []
    for vuelo_data in json_data['data']:
        iata = vuelo_data['flight']['iata'] 
        if iata:
            vuelos.append(f"Ticket: {iata}")

    return vuelos

def obtener_vuelosAPI(ticket):

    params = {
        'access_key': api_key,
        'flight_iata' : ticket,
        'offset': 0   
    }

    apiresponse = requests.get(endpoint, params=params)

    if apiresponse.status_code != 200: 
        raise Exception(f"Error en la solicitud de la API: {apiresponse.status_code}")

    return apiresponse.json()
"""
    Solicita vuelos asociados a un código IATA a través de una API.

    Args:
        iata (str): Código IATA de un aeropuerto.

    Raises:
        Exception: Si la solicitud a la API falla.

    Returns:
        dict: Datos de los vuelos obtenidos desde la API.
"""

def crear_vuelos(json_data):
    vuelos = []
    for vuelo_data in json_data['data']:
        vuelo = {
            "origen": vuelo_data['departure']['airport'],
            "destino": vuelo_data['arrival']['airport'],
            "hrorigen": redondea_hora(vuelo_data['departure']['estimated']),
            "hrdestino": redondea_hora(vuelo_data['arrival']['estimated']),
            "hora realOr": formato_hora_minuto(vuelo_data['departure']['estimated']),
            "hora realDes": formato_hora_minuto(vuelo_data['arrival']['estimated']),
            "fecha abreviadaOr": formato_dia_mes(vuelo_data['departure']['estimated']),
            "fecha abreviadaDes": formato_dia_mes(vuelo_data['arrival']['estimated']),
            "ciudadOr": predicc(vuelo_data['departure']['iata']),
            "ciudadDes": predicc(vuelo_data['arrival']['iata']),
            "aereolinea": vuelo_data['airline']['name'],
            "iataorigen": vuelo_data['departure']['iata'],
            "iatadestino": vuelo_data['arrival']['iata'],
            "iata": vuelo_data['flight']['iata']
        }
        vuelos.append(vuelo)
    
    return vuelos
"""
    Crea una lista de vuelos a partir de los datos JSON obtenidos.

    Args:
        json_data (dict): Datos de vuelos en formato JSON obtenidos de la API.

    Returns:
        list: Lista de vuelos con los campos relevantes procesados.
"""