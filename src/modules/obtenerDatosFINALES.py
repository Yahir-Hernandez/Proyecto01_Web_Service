
import os
from obtenervuelos import obtener_vuelosCiudad, obtener_vuelosPorIATA
from cacheyEscritura import guardar_cache
from obtenerclimas import weather, buscar_clima

carpeta_destino = os.path.join(os.path.dirname(__file__), '../datosFinales') #definir una carpeta donde gaurdar el json
nombre_archivo= f'info_final.json' 

ruta = os.path.join(carpeta_destino, nombre_archivo) #Definir la ruta del archivo para guardar los objetos

def obtenerDatosporCiudad(origen, destino):

    vuelos = obtener_vuelosCiudad(origen, destino)
    climaorigen = weather(origen)
    climadestino = weather(destino)

    vuelos_combinados = []

    for vuelo in vuelos:
        hr_origen = vuelo['hrorigen']
        hr_destino = vuelo['hrdestino']

        clima_para_origen = buscar_clima(climaorigen, origen, hr_origen)
        clima_para_destino = buscar_clima(climadestino, destino, hr_destino)

        if clima_para_origen and clima_para_destino: 
            vuelo['clima_origen'] = clima_para_origen
            vuelo['clima_destino'] = clima_para_destino

            vuelos_combinados.append(vuelo)

    guardar_cache(ruta, vuelos_combinados)

    return print(vuelos_combinados)

def obtenerDatosporIATA(iata):

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

    return print(vuelos_combinados)


obtenerDatosporCiudad("Ciudad de México", "Monterrey")
