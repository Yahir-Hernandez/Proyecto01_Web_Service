import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.cacheyEscritura import guardar_cache, decide_SiBorrarCache
from utils.horasyTiempo import redondea_hora, hoy
from utils.obtenervuelos import obtener_vuelo
from utils.predicc import predicc as pc
from utils.traductor import traducirExcepcion
from utils.obtenerclimas import weather, buscar_clima

def datosCiudad(destino):

    try:

        decide_SiBorrarCache()
    
        carpeta_destino = os.path.join(os.path.dirname(__file__), '../utils/cache') 
        nombre_archivo= f'climas_Consultados.json' 

        ruta = os.path.join(carpeta_destino, nombre_archivo) 

        clima = []

        destinoPc = pc(destino)
        clima_dest = weather(destinoPc)

        hora = redondea_hora(hoy())
        encontrado = buscar_clima(clima_dest, hora)
        clima.append(encontrado)

        guardar_cache(ruta, clima)
        return clima
    
    except Exception as e:

        return traducirExcepcion(str(e))
    

"""
    Combina los datos de vuelos entre dos ciudades con sus respectivos climas y guarda el resultado en caché.

    Args:
        origen (str): Nombre de la ciudad de origen.
        destino (str): Nombre de la ciudad de destino.

    Returns:
        list: Lista de vuelos combinados con los datos climáticos del origen y destino.
    
    Raises:
        Exception: Si ocurre algún error en el proceso, se traduce el mensaje de excepción.
"""

def datosTicket(ticket):

    try:

        decide_SiBorrarCache()

        carpeta_destino = os.path.join(os.path.dirname(__file__), '../utils/cache') 
        nombre_archivo= f'tickets_Consultados.json' 

        ruta = os.path.join(carpeta_destino, nombre_archivo) 

        vuelo = obtener_vuelo(ticket)

        vuelos_combinados = []
        origen = vuelo[0]['ciudadOr']
        destino = vuelo[0]['ciudadDes']
        hr_origen = vuelo[0]['hrorigen']
        hr_destino = vuelo[0]['hrdestino']
        
        climaorigen = weather(origen)
        climadestino = weather(destino)

        clima_para_origen = buscar_clima(climaorigen, hr_origen)
        clima_para_destino = buscar_clima(climadestino, hr_destino)

        if clima_para_origen and clima_para_destino:
            vuelo[0]['clima_origen'] = clima_para_origen
            vuelo[0]['clima_destino'] = clima_para_destino

        vuelos_combinados.append(vuelo[0])
        guardar_cache(ruta, vuelos_combinados)

        return vuelos_combinados

    except Exception as e:
        return traducirExcepcion(str(e))
    
     
"""
    Combina los datos de vuelos obtenidos a través de un código IATA con los climas de las ciudades de origen y destino,
    y guarda el resultado en caché.

    Args:
        iata (str): Código IATA de la ciudad para la que se desean obtener los datos.

    Returns:
        list: Lista de vuelos combinados con los datos climáticos del origen y destino.
    
    Raises:
        Exception: Si ocurre algún error en el proceso, se traduce el mensaje de excepción.
"""

