import sys
import os
# Añadir el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.obtenerDatosFINALES import obtenerDatosporIATA, obtenerDatosporCiudad
from utils.predicc import predicc
from services.obtenerclimas import verificaEnCacheClima
from services.obtenervuelos import verificaEnCacheCiudad

'''if __name__ == '__main__':

    print("Prueba de errores en el metodo 'obtenerDatosporCiudad'")
    print("________________________________________________________\n\n")

    origen = input("Ingresa la ciudad de origen: ")
    destino = input("Ingresa la ciudad de destino: ")

    print(f"Origen: {predicc(origen)}, destino: {predicc(destino)}")

    obtenerDatosporCiudad(origen, destino)'''

print("Prueba de errores en el metodo 'obtenerDatosporIATA'")
print("________________________________________________________\n\n")

iata = input("Ingresa la iata correcta de un vuelo que sale hoy:  ")

obtenerDatosporIATA(iata)


'''carpeta_destino = os.path.join(os.path.dirname(__file__), '../cache') #definir una carpeta donde gaurdar los objetos
nombre_archivo= f'climas_cache.json'
ruta = os.path.join(carpeta_destino, nombre_archivo)
climas1 = verificaEnCacheClima(ruta, "Monterrey")
climas2 = verificaEnCacheClima(ruta, "Ciudad de México")
carpeta_destino = os.path.join(os.path.dirname(__file__), '../cache') #definir una carpeta donde gaurdar los objetos
nombre_archivo= f'vuelos_cache.json'
ruta = os.path.join(carpeta_destino, nombre_archivo)

vuelos = verificaEnCacheCiudad(ruta,  "MTY","MEX")

for vuelo in vuelos:
    for clima in climas1:
        if clima["Fecha y hora"] == vuelo["hrorigen"] and clima['Ciudad']==vuelo['ciudadOr']:
            print("_____________Clima_origen_____________")
            print(clima)
    for clima in climas2:
        if clima["Fecha y hora"] == vuelo["hrdestino"] and clima['Ciudad']==vuelo['ciudadDes']:
            print("____________Clima_destino____________")
            print(clima)
            print("________________vuelo_________________-")
            print(vuelo)'''



