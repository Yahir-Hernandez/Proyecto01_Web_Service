import os
import pandas as pd
import requests
import sys

from utils.horasyTiempo import fecha_hoy, fecha_final, ayer
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.iatas import iatasC
from utils.cacheyEscritura import cargar_cache
from utils.cacheyEscritura import guardar_cache
from utils.predicc import predicc as pc
from utils.horasyTiempo import convertDT_a_CST, formato_ano_mes, formato_hora_minuto
from utils.traductor import traducir_descripcion, traducir_main


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

    return climas

def solicitarAPIClima(lugar):

    key = "bafa68a647e077182f2e167abc8648dd"
    lat, lon = obtener_coordenadas(lugar) #valor la latitud y longitud del lugar
    url = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={key}&units=metric&lang=es"
    rp = requests.get(url) 
    
    # status_code sera igual a 200 si la solicitud fue recibida, entendida y procesada con éxito.
    if rp.status_code != 200:
        raise Exception(f"Error en la solicitud de la API: {rp.status_code}")
    
    return rp.json()

def solicitarAPIClimaHistorico(lugar):
    '''Solicita datos de horas anteriores a la hora actual de este mismo dias
    @lugar: ciudad que se quiere consulta climar
    @return: respuesta de la api del clima'''
    key = "bafa68a647e077182f2e167abc8648dd"
    lat, lon = obtener_coordenadas(lugar)  # valor la latitud y longitud del lugar
    start = ayer()
    end = fecha_final(fecha_hoy())
    url = f"https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&start={start}&end={end}&appid={key}&units=metric"
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
            if ciudad == clima['Ciudad']:
                climas_encontrados.append(clima)

        # Si se encontraron climas, devolverlos
        if climas_encontrados:
            print("Coincidencias de clima encontradas en caché.")
            return climas_encontrados

    # Si no hay coincidencias en el caché, solicitar nuevos datos a la API
    print("Clima no encontrado en caché. Solicitando datos a la API.")
    data = solicitarAPIClimaHistorico(ciudad)
    climas_creados = crear_clima(data, ciudad)
    guardar_cache(ruta, climas_creados)

    data2 = solicitarAPIClima(ciudad)
    climas_creados2 = crear_clima(data2, ciudad)
    guardar_cache(ruta, climas_creados2)

    return climas_creados + climas_creados2

def obtener_coordenadas(lugar):

    if not lugar or lugar == "":
        raise Exception("Por favor, selecciona un lugar válido")
    
    # Construir la ruta al archivo CSV
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/dataset.csv'))
    
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

def buscar_clima(clima_data, ciudad, hora):

    for clima in clima_data:
        if clima['Fecha y hora']==hora and clima['Ciudad']==ciudad:
            return clima
    return None


def crear_clima(json_data, ciudad):
    climas = []
    
    for clima_data in json_data.get('list', []):
        #Usar get en lugar de acceder directamente a las claves y listas.
        #Evitar excepciones si una clave no está presente en el diccionario.
        clima = {
            "Ciudad": ciudad,
            "Clima": traducir_descripcion(clima_data.get('weather')[0].get('main')),
            "Descripcion": traducir_main(clima_data.get('weather')[0].get('id')),
            "Temperatura": clima_data.get('main').get('temp'),
            "Nubosidad": clima_data.get('clouds').get('all'),
            "Presion atmosferica": clima_data.get('main').get('pressure'),
            "Temperatura minima": clima_data.get('main').get('temp_min'),
            "Temperatura maxima": clima_data.get('main').get('temp_max'),
            "Velocidad del viento": clima_data.get('wind').get('speed'),
            "Direccion del viento": clima_data.get('wind').get('deg'),
            "Fecha y hora": convertDT_a_CST(clima_data.get('dt')),
            "Fecha real": formato_ano_mes(convertDT_a_CST(clima_data.get('dt'))),
            "Humedad": clima_data.get('main').get('humidity'),
            "Visibilidad": clima_data.get('visibility'),
        }
        climas.append(clima)
    
    return climas
