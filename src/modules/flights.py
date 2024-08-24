from iatas import iatasC
from datetime import datetime as tm
from prediccion import predicc as pc
import requests
import json
import time
import os

#Si se ingresas origen en CDMX, se debe de ingresar destino
#en caso de que origen es diferente de CDMX, entonces destino es igual a ""
#Si se ingresa flight_iata se buscara el vuelo en concreto
def obtener_vuelos(origen, destino=None, flight_iata=None):
    # Clave de acceso para la API
    api_key = 'USA_TU_KEY'
    # Endpoint de la API para obtener información de vuelos
    endpoint = 'http://api.aviationstack.com/v1/flights'
    
    # Verificar si se ha proporcionado un origen
    if not origen:
        return []  # Si no se proporciona origen, devolver False
    
    # Convertir el nombre del aeropuerto de origen y destino en códigos IATA
    dep_iata = iatasC(origen)  # Función que convierte el nombre del origen en código IATA
    arr_iata = "MEX" if not destino else iatasC(destino)  # Si no se proporciona destino, usar "MEX" como destino
    
    # Si el origen y el destino son el mismo aeropuerto, devolver False
    if dep_iata ==  arr_iata :
        return []
    
    # Preparar los parámetros para la solicitud a la API
    params = {
        'access_key': api_key,
        'dep_iata': dep_iata,
        'arr_iata': arr_iata,
        'limit': 100,  # Limitar el número de resultados a 100 por solicitud
        'offset': 0    # Offset inicial para la paginación
    }

    all_flights = []  # Lista para almacenar todos los vuelos obtenidos
    codigo_iata = flight_iata.strip() if flight_iata else ""  # Limpiar espacios en blanco alrededor del código IATA, si se proporciona

    # Hacer solicitudes a la API hasta que se obtengan todos los resultados
    while True:
        response = requests.get(endpoint, params=params)  # Realizar la solicitud a la API
        flight_data = response.json()  # Convertir la respuesta en formato JSON

        # Si se proporciona un código IATA específico, buscar vuelos que coincidan
        if flight_iata:
            if 'data' in flight_data:
                for flight in flight_data['data']:
                    if flight["flight"]["iata"].upper() == codigo_iata.upper():
                        return [flight]  # Devolver el vuelo que coincide con el código IATA

        # Si se encontraron datos de vuelos, filtrarlos y añadirlos a la lista
        if 'data' in flight_data:
            all_flights.extend(filt_fecha(flight_data))  # Función que filtra los datos según la fecha
        else:
            break  # Salir del bucle si no se encontró la clave 'data'

        # Si la respuesta contiene menos de 100 resultados, no hay más páginas, salir del bucle
        if len(flight_data['data']) < 100:
            break

        # Incrementar el offset para la siguiente página de resultados
        params['offset'] += 100
        time.sleep(1)  # Pausar la ejecución durante 1 segundo para evitar sobrecargar la API

    return all_flights  # Devolver la lista completa de vuelos obtenidos

def filt_fecha(doc):
    # Fecha de hoy en formato YYYY-MM-DD
    fecha = tm.today().date()
    
    # Filtra los vuelos que se hicieron hoy
    vuelos_hoy = []
    for x in doc["data"]:
        # Extrae la fecha de llegada estimada
        llegada_estim = x["arrival"]["estimated"]
        
        # Convierte la cadena de fecha y hora en un objeto datetime
        fecha_llegada = tm.fromisoformat(llegada_estim.replace("Z", "+00:00")).date()
        
        # Compara la fecha de llegada con la fecha de hoy
        if fecha_llegada == fecha:
            vuelos_hoy.append(x)
    
    return vuelos_hoy

if __name__ == "__main__":
    # Solicitar datos al usuario
    origen = input("Ciudad de origen: ")
    destino = input("Ciudad de destino: ")
    flight_iata = input("Código IATA del vuelo (opcional, presiona Enter para omitir): ")

    # Ejecutar la función
    obtener_vuelos(origen, destino, flight_iata)
