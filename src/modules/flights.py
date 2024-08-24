from iatas import iatasC
from datetime import datetime as tm
from vuelo import Vuelo
from datetime import datetime
import requests
import json
import os

#Si se ingresas origen en CDMX, se debe de ingresar destino
#en caso de que origen es diferente de CDMX, entonces destino es igual a ""
#Si se ingresa flight_iata se buscara el vuelo en concreto
def obtener_vuelosPorCiudad(origen, destino):
    # Clave de acceso para la API
    api_key = 'c4e545f6c150f757d7dd30a3b0501599'
    # Endpoint de la API para obtener información de vuelos
    endpoint = 'http://api.aviationstack.com/v1/flights'
    
    # Verificar si se ha proporcionado un origen
    if not origen or not destino:
        raise ValueError("Selecciona un origen válido")  # Si no se proporciona origen, devolver False
    
    # Convertir el nombre del aeropuerto de origen y destino en códigos IATA
    dep_iata = iatasC(origen)  # Función que convierte el nombre del origen en código IATA
    arr_iata = iatasC(destino)  # Función que convierte el nombre del destino en código IATA

    if dep_iata != 'MEX' and arr_iata != 'MEX':
        raise ValueError("La ciudad de origen o destino debe de ser la Ciudad de México.")
    
    # Si el origen y el destino son el mismo aeropuerto, devolver False
    if dep_iata ==  arr_iata :
        raise ValueError("La ciudad de origen y destino deben ser distintas") 
    
    # Preparar los parámetros para la solicitud a la API
    params = {
        'access_key': api_key,
        'dep_iata': dep_iata,
        'arr_iata': arr_iata,
        #'flight_date' : date,
        'limit': 100,  # Limitar el número de resultados a 100 por solicitud
        'offset': 0    # Offset inicial para la paginación
    }

    try:
        apiresponse = requests.get(endpoint, params=params)

        if apiresponse.status_code != 200: #confirmar el éxito de la respuesta del API
            raise Exception(f"Error en la solicitud de la API: {apiresponse.status_code}")
    
        data = apiresponse.json()

        carpeta_destino = os.path.join(os.path.dirname(__file__), '../data') #definir una carpeta donde gaurdar el json
        nombre_archivo= 'vuelos.json' 

        #asegurarse de que la carpeta destino exista
        os.makedirs(carpeta_destino, exist_ok=True)

        ruta = os.path.join(carpeta_destino, nombre_archivo) #Definir la ruta del json

        with open(ruta, 'w') as archivo:
            json.dump(data, archivo, indent=4) # guardar los datos del json en la carpeta especificada

    except:
        return "Error generando el json"
    
    return crear_vuelos(data)
   
def crear_vuelos(json_data):
    vuelos = []
    for vuelo_data in json_data['data']:
        origen = vuelo_data['departure']['airport']
        destino = vuelo_data['arrival']['airport']
        hrorigen = vuelo_data['departure']['estimated']
        hrdestino = vuelo_data['arrival']['estimated']
        ciudadOr = vuelo_data['departure']['timezone']
        ciudadDes = vuelo_data['arrival']['timezone']
        
        vuelo = Vuelo(
            origen=origen,
            destino=destino,
            hrorigen=hrorigen,
            hrdestino=hrdestino,
            ciudadOr=ciudadOr,
            ciudadDes=ciudadDes
        )
        print(vuelo)
        vuelos.append(vuelo)
    
    return vuelos

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

    # Ejecutar la función
obtener_vuelosPorCiudad("Ciudad de Mexico", "Monterrey")
