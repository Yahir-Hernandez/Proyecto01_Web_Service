from iatas import iatasC
from prediccion import predicc
from cacheyEscritura import cargar_cache
from cacheyEscritura import guardar_cache
from horasyTiempo import reescribe_hora
import requests
import os 

#Si se ingresas origen en CDMX, se debe de ingresar destino

# Clave de acceso para la API
api_key = 'c4e545f6c150f757d7dd30a3b0501599'
# Endpoint de la API para obtener información de vuelos
endpoint = 'http://api.aviationstack.com/v1/flights'
    
def obtener_vuelosCiudad(origen, destino):

    origen.replace(" ", "")
    destino.replace(" ", "")

    # Verificar si se ha proporcionado un origen
    if not origen or not destino or origen=="" or destino=="":
        raise ValueError("Selecciona un origen o destino válidos")  # Si no se proporciona origen, devolver False

    # Convertir el nombre del aeropuerto de origen y destino en códigos IATA
    #agregar try except
    dep_iata = iatasC(origen)  
    arr_iata = iatasC(destino)  

    if dep_iata != 'MEX' and arr_iata != 'MEX':
        raise ValueError("La ciudad de origen o destino debe de ser la Ciudad de México.")
    
    # Si el origen y el destino son el mismo aeropuerto, devolver False
    if dep_iata ==  arr_iata :
        raise ValueError("La ciudad de origen y destino deben ser distintas") 

    carpeta_destino = os.path.join(os.path.dirname(__file__), '../cache') #definir una carpeta donde gaurdar los objetos
    nombre_archivo= f'vuelos_cache.json' 
    ruta = os.path.join(carpeta_destino, nombre_archivo) #Definir la ruta del archivo para guardar los objetos

    vuelos = verificaEnCacheCiudad(ruta, dep_iata, arr_iata)

    return vuelos

def verificaEnCacheCiudad(ruta, dep_iata, arr_iata):

    # Cargar los vuelos desde el archivo de caché si existe
    data_cache = cargar_cache(ruta)
    vuelos_encontrados = []

    if data_cache:
        print("Verificando coincidencias en caché...")

        # Buscar en la lista de vuelos los que coincidan con la ciudad proporcionada
        for vuelo in data_cache:
            if vuelo['iataorigen'] == dep_iata and vuelo['iatadestino'] == arr_iata:
                vuelos_encontrados.append(vuelo)

        # Si se encontraron vuelos, devolverlos
        if vuelos_encontrados:
            print("Coincidencias de vuelo encontradas en caché.")
            return vuelos_encontrados

    # Si no hay coincidencias en el caché, solicitar nuevos datos a la API
    print("Vuelos no encontrados en caché. Solicitando vuelos a la API.")
    data = obtener_vuelosAPI_ciudad(dep_iata, arr_iata)
    vuelos = crear_vuelos(data)
    guardar_cache(ruta, vuelos)

    return vuelos

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

def obtener_vuelosPorIATA(iata):

    iata = iata.replace(" ", "")  # Reemplazar correctamente los espacios y asignar a la variable


    if not iata or iata=="":
        raise Exception("Por favor selecciona un iata válido")
    
    carpeta_destino = os.path.join(os.path.dirname(__file__), '../cache') #definir una carpeta donde gaurdar el json
    nombre_archivo= f'vuelos_cache.json' 

    ruta = os.path.join(carpeta_destino, nombre_archivo) #Definir la ruta del archivo para guardar los objetos

    vuelo = verificaEnCacheIATA(ruta, iata)

    return vuelo

def verificaEnCacheIATA(ruta, iata):
    # Cargar los vuelos desde el archivo de caché si existe
    data_cache = cargar_cache(ruta)
    vuelos_encontrados = []

    if data_cache:
        print("Verificando coincidencias en caché...")

        # Buscar en la lista de vuelos los que coincidan con el IATA proporcionado
        for vuelo in data_cache:
            if vuelo['iata'] == iata:
                vuelos_encontrados.append(vuelo)

        # Si se encontraron vuelos, devolverlos
        if vuelos_encontrados:
            print("Coincidencias de vuelo encontradas en caché.")
            return vuelos_encontrados

    # Si no hay coincidencias en el caché, solicitar nuevos datos a la API
    print("Vuelo no encontrado en caché. Solicitando datos de la API.")
    data_nueva = obtener_vuelosAPI_IATA(iata)
    vuelo = crear_vuelos(data_nueva)
    guardar_cache(ruta, vuelo)

    return vuelo

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

def crear_vuelos(json_data):
    vuelos = []
    for vuelo_data in json_data['data']:
        vuelo = {
            "origen": vuelo_data['departure']['airport'],
            "destino": vuelo_data['arrival']['airport'],
            "hrorigen": reescribe_hora(vuelo_data['departure']['estimated']),
            "hrdestino": reescribe_hora(vuelo_data['arrival']['estimated']),
            "ciudadOr": predicc(vuelo_data['departure']['iata']),
            "ciudadDes": predicc(vuelo_data['arrival']['iata']),
            "Aereolínea:": vuelo_data['airline']['name'],
            "iataorigen": vuelo_data['departure']['iata'],
            "iatadestino": vuelo_data['arrival']['iata'],
            "iata": vuelo_data['flight']['iata']
        }
        vuelos.append(vuelo)
    
    return vuelos