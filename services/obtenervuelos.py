from utils.iatas import iatasC
from utils.predicc import predicc
from utils.cacheyEscritura import cargar_cache, guardar_cache
from utils.horasyTiempo import reescribe_hora, formato_hora_minuto, formato_ano_mes
import requests
import os 

#Si se ingresas origen en CDMX, se debe de ingresar destino

# Clave de acceso para la API
api_key = '57fdee256d89b56c321e90f5f9a8cc17'
# Endpoint de la API para obtener información de vuelos
endpoint = 'http://api.aviationstack.com/v1/flights'
    
def obtener_vuelosCiudad(origen, destino):

    origen.replace(" ", "")
    destino.replace(" ", "")

    # Verificar si se ha proporcionado un origen
    if not origen or not destino or origen=="" or destino=="":
        raise Exception("Selecciona un origen o destino válidos.")  

    # Convertir el nombre del aeropuerto de origen y destino en códigos IATA
    
    dep_iata = iatasC(origen)  
    arr_iata = iatasC(destino)  

    if dep_iata != 'MEX' and arr_iata != 'MEX':
        raise Exception("La ciudad de origen o destino debe de ser la Ciudad de México.")
    
    # Si el origen y el destino son el mismo aeropuerto, devolver False
    if dep_iata ==  arr_iata :
        raise Exception("La ciudad de origen y destino deben ser distintas.") 

    carpeta_destino = os.path.join(os.path.dirname(__file__), '../cache') #definir una carpeta donde gaurdar los objetos
    nombre_archivo= f'vuelos_cache.json' 
    ruta = os.path.join(carpeta_destino, nombre_archivo) #Definir la ruta del archivo para guardar los objetos

    vuelos = verificaEnCacheCiudad(ruta, dep_iata, arr_iata)

    return vuelos
"""
    Obtiene vuelos desde una ciudad de origen a una ciudad de destino, verificando primero en el caché
    y solicitando datos de la API si no se encuentran coincidencias.

    Args:
        origen (str): Nombre de la ciudad de origen.
        destino (str): Nombre de la ciudad de destino.

    Raises:
        Exception: Si no se proporcionan un origen y un destino válidos.
        Exception: Si ninguno de los aeropuertos es la Ciudad de México (MEX).
        Exception: Si el aeropuerto de origen y destino son los mismos.

    Returns:
        list: Lista de vuelos desde la ciudad de origen a la ciudad de destino.
    """

def verificaEnCacheCiudad(ruta, dep_iata, arr_iata):

    # Cargar los vuelos desde el archivo de caché si existe
    data_cache = cargar_cache(ruta)
    vuelos_encontrados = []

    if data_cache:

        # Buscar en la lista de vuelos los que coincidan con la ciudad proporcionada
        for vuelo in data_cache:
            if vuelo['iataorigen'] == dep_iata and vuelo['iatadestino'] == arr_iata:
                vuelos_encontrados.append(vuelo)

        # Si se encontraron vuelos, devolverlos
        if vuelos_encontrados:

            return vuelos_encontrados

    # Si no hay coincidencias en el caché, solicitar nuevos datos a la API
    data = obtener_vuelosAPI_ciudad(dep_iata, arr_iata)
    vuelos = crear_vuelos(data)
    guardar_cache(ruta, vuelos)

    return vuelos

"""
    Verifica si existen vuelos entre dos ciudades en el caché y, si no, solicita los datos a la API.

    Args:
        ruta (str): La ruta del archivo de caché.
        dep_iata (str): Código IATA de la ciudad de origen.
        arr_iata (str): Código IATA de la ciudad de destino.

    Returns:
        list: Lista de vuelos encontrados o solicitados.
    """

def obtener_vuelosAPI_ciudad(dep_iata, arr_iata):
     
    # Preparar los parámetros para la solicitud a la API
    params = {
        'access_key': api_key,
        'dep_iata': dep_iata,
        'arr_iata': arr_iata,
        'limit': 100,  # Limitar el número de resultados a 100 por solicitud
        'offset': 0    # Offset inicial para la paginación
    }

    apiresponse = requests.get(endpoint, params=params)

    if apiresponse.status_code != 200: #confirmar el éxito de la respuesta del API
        raise Exception(f"Error en la solicitud de la API: {apiresponse.status_code}")

    return apiresponse.json()

"""
    Solicita vuelos entre dos ciudades a través de una API.

    Args:
        dep_iata (str): Código IATA de la ciudad de origen.
        arr_iata (str): Código IATA de la ciudad de destino.

    Raises:
        Exception: Si la solicitud a la API falla.

    Returns:
        dict: Datos de los vuelos obtenidos desde la API.
    """

def obtener_vuelosPorIATA(iata):

    iata.replace(" ", "")
    iata.replace("%20","")

    if not iata or iata=="":
        raise Exception("Por favor selecciona un iata válido.")
    
    carpeta_destino = os.path.join(os.path.dirname(__file__), '../cache') #definir una carpeta donde gaurdar el json
    nombre_archivo= f'vuelos_iata_cache.json' 

    ruta = os.path.join(carpeta_destino, nombre_archivo) #Definir la ruta del archivo para guardar los objetos

    vuelo = verificaEnCacheIATA(ruta, iata)

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
def verificaEnCacheIATA(ruta, iata):
    # Cargar los vuelos desde el archivo de caché si existe
    data_cache = cargar_cache(ruta)
    vuelos_encontrados = []

    if data_cache:

        # Buscar en la lista de vuelos los que coincidan con el IATA proporcionado
        for vuelo in data_cache:
            if vuelo['iata'].upper() == iata.upper():
                vuelos_encontrados.append(vuelo)

        # Si se encontraron vuelos, devolverlos
        if vuelos_encontrados:
            return vuelos_encontrados

    # Si no hay coincidencias en el caché, solicitar nuevos datos a la API
    data_nueva = obtener_vuelosAPI_IATA(iata)
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

def obtener_vuelosAPI_IATA(iata):

    params = {
        'access_key': api_key,
        'flight_iata' : iata,
        'limit': 100,  # Limitar el número de resultados a 100 por solicitud
        'offset': 0    # Offset inicial para la paginación
    }

    apiresponse = requests.get(endpoint, params=params)

    if apiresponse.status_code != 200: #confirmar el éxito de la respuesta del API
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
            "hrorigen": reescribe_hora(vuelo_data['departure']['estimated']),
            "hrdestino": reescribe_hora(vuelo_data['arrival']['estimated']),
            "hora realOr": formato_hora_minuto(vuelo_data['departure']['estimated']),
            "hora realDes": formato_hora_minuto(vuelo_data['arrival']['estimated']),
            "fecha abreviadaOr": formato_ano_mes(vuelo_data['departure']['estimated']),
            "fecha abreviadaDes": formato_ano_mes(vuelo_data['arrival']['estimated']),
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