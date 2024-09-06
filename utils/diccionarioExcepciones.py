
def traducirExcepción(msg):

    exception ={

        "Por favor selecciona un lugar válido para solicitar el clima." : 101, #Error (Sin parámtero en weather)
        "No se pudo leer o no existe el archivo SCV dataset.": 102, #Error (No existe o pandas no pudo leer el SCV de coordenadas)
        "Selecciona un origen o destino válidos." : 103, #Error (Sin origen o destino en obtener_vuelosCiudad)
        "La ciudad de origen o destino debe de ser la Ciudad de México.": 104, #Error (Ninguno de los parámetros en obtener_vuelosCiudad es la CDMX)
        "La ciudad de origen y destino deben ser distintas." : 105, #Error (Los parámetros en obtener_vuelosCiudad son iguales)
        "Por favor selecciona un iata válido." : 106, #Error (Sin parámtero en obtener_vuelosPorIATA)
        "No se encontraron coincidencias para esa ciudad." : 107, #Error (Predicc no encontró coincidencias con fuzzywuzzy)
        "No se pudo leer o no existe el archivo CSV IATAS." : 108, 
        "No se encontró el IATA." : 109, #Error (iatasC no encontró coincidencias)
        "Error en la solicitud de la API: 400": 200,  # Error (Mal Request)
        "Error en la solicitud de la API: 401": 201,  # Error (No autorizado por la API)
        "Error en la solicitud de la API: 403": 203,  # Error (Prohibido)
        "Error en la solicitud de la API: 404": 204,  # Error (No encontrado)
        "Error en la solicitud de la API: 500": 300,  # Error (Error Interno del Servidor)
        "Error en la solicitud de la API: 502": 302,  # Error (Mala Puerta de Enlace)
        "Error en la solicitud de la API: 503": 303,  # Error (Servicio No Disponible)
        
    }

    for key, value in exception:

        if key == msg:
            return [value]
    
    return [500] # 500 es error desconocido

    