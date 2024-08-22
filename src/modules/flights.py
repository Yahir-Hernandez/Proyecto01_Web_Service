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
def obtener_vuelos(origen,  destino=None, flight_iata=None):
    api_key = 'USA_Tu_KEY'
    endpoint = 'http://api.aviationstack.com/v1/flights'
    
     # Ruta relativa a la carpeta donde quieres guardar el archivo JSON
    carpeta_destino = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/data'))
    if origen == "":
        return False

    #Si el destino es nulo entonces el distino es el AICM
    dep_iata = iatasC(origen)
    if destino == "":
        arr_iata = "MEX"
        if dep_iata == "MEX":
            return False
    else:
        arr_iata = iatasC(destino)
        
    codigo_iata = "" if (flight_iata == "") else flight_iata.replace(" ", "")

    # Parámetros iniciales para la solicitud
    params = {
        'access_key': api_key,
        'dep_iata': dep_iata,
        'arr_iata': arr_iata,
        'limit': 100,
        'offset': 0
    }
    ori = pc(origen)
    des = pc(destino) if (destino != "") else "Ciudad de Mexico"
    all_flights = []
    while True:
        response = requests.get(endpoint, params=params)
        flight_data = response.json()

        if flight_iata !=  "":
            if 'data' in flight_data:
                for flight in flight_data['data']:
                    if flight["flight"]["iata"].upper() == codigo_iata.upper():
                        dat = {"data": flight}
                        # Ruta completa del archivo JSON
                        ruta_completa = os.path.join(carpeta_destino, f"{dep_iata}_{arr_iata}.json")
                        with open(ruta_completa, 'w', encoding="UTF-8") as archivo_json:
                            json.dump(dat, archivo_json, indent=4)
                        return True

        if 'data' in flight_data:
            all_flights.extend(filt_fecha(flight_data))
            print(len(all_flights))
        else:
            print("No se encontró la clave 'data'. Revisa la respuesta de la API:", flight_data)
            break

        if len(flight_data['data']) < 100:
            break

        params['offset'] += 100
        time.sleep(1)
    ruta_completa = os.path.join(carpeta_destino,f"{ori}_{des}.json")
    with open(ruta_completa, 'w', encoding="UTF-8") as archivo_json:
        json.dump({"data": all_flights}, archivo_json, indent=4)

    print(f"Todos los datos han sido almacenados en vuelos_{ori}_{des}.json")
    return True

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
