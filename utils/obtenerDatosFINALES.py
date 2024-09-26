import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.obtenervuelos import obtener_vuelosCiudad, obtener_vuelosPorIATA
from utils.cacheyEscritura import guardar_cache
from utils.predicc import predicc as pc
from utils.traductor import traducirExcepcion
from utils.obtenerclimas import weather, buscar_clima

def obtenerDatosporCiudad(origen, destino):

    carpeta_destino = os.path.join(os.path.dirname(__file__), '../cache') #definir una carpeta donde gaurdar el json
    nombre_archivo= f'info_final_ciudad.json' 

    ruta = os.path.join(carpeta_destino, nombre_archivo) #Definir la ruta del archivo para guardar los objetos

    try:

        vuelos = obtener_vuelosCiudad(origen, destino)
        climaorigen = weather(origen)
        climadestino = weather(destino)

        ciudadO = pc(origen)
        CiudadD = pc(destino)

        vuelos_combinados = []

        for vuelo in vuelos:
            hr_origen = vuelo['hrorigen']
            hr_destino = vuelo['hrdestino']

            clima_para_origen = buscar_clima(climaorigen, ciudadO, hr_origen)
            clima_para_destino = buscar_clima(climadestino, CiudadD, hr_destino)

            if clima_para_origen and clima_para_destino: 
                vuelo['clima_origen'] = clima_para_origen
                vuelo['clima_destino'] = clima_para_destino

                vuelos_combinados.append(vuelo)

        guardar_cache(ruta, vuelos_combinados)
        return vuelos_combinados
    
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
    
def obtenerDatosporIATA(iata):

    carpeta_destino = os.path.join(os.path.dirname(__file__), '../cache') #definir una carpeta donde gaurdar el json
    nombre_archivo= f'info_final_iata.json' 

    ruta = os.path.join(carpeta_destino, nombre_archivo) #Definir la ruta del archivo para guardar los objetos

    try:
        vuelos = obtener_vuelosPorIATA(iata)

        vuelos_combinados = []

        for vuelo in vuelos:

            origen = vuelo['ciudadOr']
            destino = vuelo['ciudadDes']
            hr_origen = vuelo['hrorigen']
            hr_destino = vuelo['hrdestino']

            climaorigen = weather(origen)
            climadestino = weather(destino)

            clima_para_origen = buscar_clima(climaorigen, origen, hr_origen)
            clima_para_destino = buscar_clima(climadestino, destino, hr_destino)

            if clima_para_origen and clima_para_destino:
                vuelo['clima_origen'] = clima_para_origen
                vuelo['clima_destino'] = clima_para_destino

                vuelos_combinados.append(vuelo)

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





