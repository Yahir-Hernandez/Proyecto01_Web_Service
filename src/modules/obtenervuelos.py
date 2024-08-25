import pickle
from iatas import iatasC
from datetime import datetime as tm
from vuelo import Vuelo
from prediccion import predicc
from cacheyEscritura import cargar_cache
from cacheyEscritura import guardar_cache
import requests
import json
import os

#Si se ingresas origen en CDMX, se debe de ingresar destino
#en caso de que origen es diferente de CDMX, entonces destino es igual a ""
#Si se ingresa flight_iata se buscara el vuelo en concreto

# Clave de acceso para la API
api_key = 'c4e545f6c150f757d7dd30a3b0501599'
# Endpoint de la API para obtener información de vuelos
endpoint = 'http://api.aviationstack.com/v1/flights'
    
def obtener_vuelosCiudad(origen, destino):

    # Verificar si se ha proporcionado un origen
    if not (origen or destino):
        raise ValueError("Selecciona una iata, origen o destino válidos")  # Si no se proporciona origen, devolver False

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
    nombre_archivo= f'vuelos_cache.pkl' 
    ruta = os.path.join(carpeta_destino, nombre_archivo) #Definir la ruta del archivo para guardar los objetos

    vuelos = verificaEnCacheCiudad(ruta, dep_iata, arr_iata)

    return imprimeVuelos(vuelos)

def imprimeVuelos(vuelos):

    for Vuelo in vuelos:
        print(Vuelo)

def imprimeVuelo(vuelo):

    print(vuelo)

def verificaEnCacheCiudad(ruta, dep_iata, arr_iata):

    # Cargar los vuelos desde el archivo de caché si existe
    data_cache = cargar_cache(ruta)
    
    if data_cache:
        vuelos_encontrados = []
        # Buscar en la lista de vuelos el que coincida con la ciudad proporcionada
        for vuelo in data_cache:
            if (vuelo.getIataorigen() == dep_iata) and (vuelo.getIatadestino() == arr_iata):
                print("Vuelos encontrado en caché")
                vuelos_encontrados.append(vuelo)
                return vuelos_encontrados

    # Si no hay vuelos en caché, solicitar nuevos datos a la API
    print("Vuelos no encontrados en caché. Solicitando vuelos a la API.")
    data = obtener_vuelosAPI_ciudad(dep_iata, arr_iata)
    vuelos = crear_vuelos(data, dep_iata, arr_iata)
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

    if not iata:
        raise ValueError("Por favor selecciona un iata válido")
    
    carpeta_destino = os.path.join(os.path.dirname(__file__), '../cache') #definir una carpeta donde gaurdar el json
    nombre_archivo= f'vuelos_cache.pkl' 

    ruta = os.path.join(carpeta_destino, nombre_archivo) #Definir la ruta del archivo para guardar los objetos

    vuelo = verificaEnCacheIATA(ruta, iata)
    
    return imprimeVuelo(vuelo)

def verificaEnCacheIATA(ruta, iata):

    # Cargar los vuelos desde el archivo de caché si existe
    data_cache = cargar_cache(ruta)

    if data_cache:
        # Buscar en la lista de vuelos el que coincida con el IATA proporcionado
        for vuelo in data_cache:
            if vuelo.getIata() == iata:
                print("Vuelo encontrado en caché")
                return vuelo
    
    print("Vuelo no encontrado en caché, solicitando datos de la API")
    # Si no hay coincidencia en el caché, solicitar nuevos datos a la API
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

def crear_vuelos(json_data, origen, destino):
    vuelos = []
    for vuelo_data in json_data['data']:
        ori = vuelo_data['departure']['airport']
        des = vuelo_data['arrival']['airport']
        hrorigen = vuelo_data['departure']['estimated']
        hrdestino = vuelo_data['arrival']['estimated']
        ciudadOr = predicc(vuelo_data['departure']['iata'])
        ciudadDes = predicc(vuelo_data['arrival']['iata'])
        iataorigen = origen
        iatadestino = destino
        iata = vuelo_data['flight']['iata']
        
        vuelo = Vuelo(
            origen=ori,
            destino=des,
            hrorigen=hrorigen,
            hrdestino=hrdestino,
            ciudadOr=ciudadOr,
            ciudadDes=ciudadDes,
            iataorigen=iataorigen,
            iatadestino=iatadestino,
            iata=iata
        )
        print(vuelo) #quitar este print, es sólo para pruebas
        vuelos.append(vuelo)
    
    return vuelos

obtener_vuelosCiudad("Ciudad de Mexico", "Madrid")
