import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
from utils.predicc import predicc
from utils.cacheyEscritura import cargar_cache, guardar_cache, guardaIATAS, carpetaCache
from utils.horasyTiempo import formato_hora_minuto, formato_dia_mes, redondea_hora
import requests

load_dotenv()

api_key = os.getenv('FLIGHT_KEY')

endpoint = 'http://api.aviationstack.com/v1/flights'
    

def obtener_vuelo(ticket):

    ticket = ticket.replace(" ", "")

    if not ticket or ticket=="":
        raise Exception("Por favor selecciona un formato de ticket válido.")
    
    carpeta_destino = os.path.join(os.path.dirname(__file__), '../utils/cache') 
    nombre_archivo= f'tickets_vuelo.json' 

    ruta = os.path.join(carpeta_destino, nombre_archivo) 

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
    carpetaCache()
    carpeta_destino = os.path.join(os.path.dirname(__file__), '../utils/cache') 
    nombre_archivo= f'tickets_vuelo.json' 

    ruta = os.path.join(carpeta_destino, nombre_archivo)

    vuelos = consulta_API()
    vuelo = crear_vuelos(vuelos)
    guardar_cache(ruta, vuelo)
    iatas = creaIATAS(vuelos)

    guardaIATAS(iatas)
    
"""
    Obtiene los códigos IATA de los vuelos y los guarda en un archivo de caché.

    Esta función consulta una API para obtener información sobre vuelos, 
    procesa la respuesta para crear un conjunto de vuelos y guarda los 
    datos en un archivo JSON en la carpeta de caché. También extrae los 
    códigos IATA de los vuelos y los guarda en un archivo de texto específico.

    Args:
        None

    Raises:
        Exception: Puede lanzar excepciones si hay errores durante la consulta 
                   a la API o al guardar los datos.

    Returns:
        None
"""
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

"""
    Realiza una solicitud a la API para obtener datos de vuelos.

    Esta función envía una solicitud GET a un endpoint de API con parámetros específicos, 
    como la clave de acceso y el código IATA de origen. Si la respuesta no es exitosa, 
    lanza una excepción.

    Args:
        None

    Raises:
        Exception: Si la respuesta de la API no es un código de estado 200.

    Returns:
        dict: La respuesta de la API en formato JSON.
"""

def creaIATAS(json_data):

    vuelos = []
    for vuelo_data in json_data['data']:
        iata = vuelo_data['flight']['iata'] 
        if iata:
            vuelos.append(f"Ticket: {iata}")

    return vuelos

"""
    Extrae los códigos IATA de los datos de vuelo proporcionados.

    Esta función itera sobre la lista de vuelos en los datos JSON, 
    extrae el código IATA de cada vuelo y lo agrega a una lista. 
    Solo se añaden los vuelos que tienen un código IATA válido.

    Args:
        json_data (dict): Datos de vuelo en formato JSON.

    Returns:
        list: Lista de códigos IATA extraídos de los datos de vuelo.
"""

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