from deep_translator import GoogleTranslator

#Corrige datos en ingles

def traducir(descripcion):
    '''Método para traducir textos generados en los json
    @param descripcion: textos que desea traducir
    '''
    # Traducir la descripción del inglés al español
    traduccion = GoogleTranslator(source='en', target='es').translate(descripcion)
    return traduccion

def traducir_main(clima_id):
    ''' Método que traduce el ID del clima a una descripción en español
    @param clima_id: ID del clima que se desea traducir
    @return: Descripción en español del clima'''

    traducciones = {
        200: "tormenta eléctrica con lluvia ligera",
        201: "tormenta eléctrica con lluvia",
        202: "tormenta eléctrica con lluvia intensa",
        210: "tormenta eléctrica ligera",
        211: "tormenta eléctrica",
        212: "tormenta eléctrica intensa",
        221: "tormenta eléctrica irregular",
        230: "tormenta eléctrica con llovizna ligera",
        231: "tormenta eléctrica con llovizna",
        232: "tormenta eléctrica con llovizna intensa",
        300: "llovizna ligera",
        301: "llovizna",
        302: "llovizna intensa",
        310: "lluvia ligera en chubascos",
        311: "lluvia en chubascos",
        312: "lluvia intensa en chubascos",
        313: "lluvia en chubascos con llovizna",
        314: "lluvia intensa en chubascos con llovizna",
        321: "llovizna en chubascos",
        500: "lluvia ligera",
        501: "lluvia moderada",
        502: "lluvia intensa",
        503: "lluvia muy intensa",
        504: "lluvia extrema",
        511: "lluvia congelante",
        520: "lluvia ligera en chubascos",
        521: "lluvia en chubascos",
        522: "lluvia intensa en chubascos",
        531: "chubascos irregulares",
        600: "nieve ligera",
        601: "nieve",
        602: "nieve intensa",
        611: "aguanieve",
        612: "lluvia ligera con nieve",
        613: "lluvia con nieve",
        615: "lluvia ligera con nieve",
        616: "lluvia con nieve",
        620: "nieve ligera en chubascos",
        621: "chubascos de nieve",
        622: "chubascos intensos de nieve",
        701: "neblina",
        711: "humo",
        721: "humo",
        731: "arena/dust",
        741: "niebla",
        751: "polvo",
        761: "polvo",
        762: "ceniza volcánica",
        771: "ráfagas",
        781: "tornado",
        800: "cielo despejado",
        801: "pocas nubes",
        802: "nubes dispersas",
        803: "nubes rotas",
        804: "nublado",
    }

    return traducciones.get(clima_id, "Descripción no disponible")


def traducir_descripcion(descripcion_clima):
    '''Método que traduce la descripción detallada del clima al español
    @param descripcion_clima: Descripción detallada del clima (e.g., "clear sky")
    @return: Descripción en español del clima
    '''
    traducciones_descripcion = {
        "Clear sky": "cielo despejado",
        "Few clouds": "pocas nubes",
        "Ccattered clouds": "nubes dispersas",
        "Broken clouds": "nubes rasgadas",
        "Overcast clouds": "cielo nuboso",
        "Shower rain": "lluvia en chubascos",
        "Rain": "lluvia",
        "light rain": "lluvia ligera",
        "moderate rain": "lluvia moderada",
        "heavy intensity rain": "lluvia intensa",
        "very heavy rain": "lluvia muy intensa",
        "extreme rain": "lluvia extrema",
        "freezing rain": "lluvia congelante",
        "light snow": "nieve ligera",
        "snow": "nieve",
        "heavy snow": "nieve intensa",
        "sleet": "aguanieve",
        "shower sleet": "chubascos de aguanieve",
        "dust": "polvo",
        "fog": "niebla",
        "sand": "arena",
        "dust": "polvo",
        "ash": "ceniza",
        "squall": "ráfaga",
        "tornado": "tornado"
    }

    return traducciones_descripcion.get(descripcion_clima, descripcion_clima)


def traducirExcepcion(msg):

    exception ={

        "Por favor selecciona un lugar válido para solicitar el clima." : "101", #Error (Sin parámtero en weather)
        "No se pudo leer o no existe el archivo SCV dataset.": "102", #Error (No existe o pandas no pudo leer el SCV de coordenadas)
        "Selecciona un origen o destino válidos." : "103", #Error (Sin origen o destino en obtener_vuelosCiudad)
        "La ciudad de origen o destino debe de ser la Ciudad de México.": "104", #Error (Ninguno de los parámetros en obtener_vuelosCiudad es la CDMX)
        "La ciudad de origen y destino deben ser distintas." : "105", #Error (Los parámetros en obtener_vuelosCiudad son iguales)
        "Por favor selecciona un iata válido." : "106", #Error (Sin parámtero en obtener_vuelosPorIATA)
        "No se encontraron coincidencias para esa ciudad." : "107", #Error (Predicc no encontró coincidencias con fuzzywuzzy)
        "No se pudo leer o no existe el archivo CSV IATAS." : "108",
        "No se encontró el IATA." : "109", #Error (iatasC no encontró coincidencias)
        "Error en la solicitud de la API: 400": "200",  # Error (Mal Request)
        "Error en la solicitud de la API: 401": "201",  # Error (No autorizado por la API)
        "Error en la solicitud de la API: 403": "203",  # Error (Prohibido)
        "Error en la solicitud de la API: 404": "204",  # Error (No encontrado)
        "Error en la solicitud de la API: 500": "300",  # Error (Error Interno del Servidor)
        "Error en la solicitud de la API: 502": "302",  # Error (Mala Puerta de Enlace)
        "Error en la solicitud de la API: 503": "303",  # Error (Servicio No Disponible)
        
    }

    for key, value in exception.items():
        if key in msg:
            return [value, msg]
    
    return ["500", "error desconocido"] # 500 es error desconocido
"""
    Traduce un mensaje de error en un código numérico específico basado en un diccionario de excepciones predefinido.

    Args:
        msg (str): Mensaje de error que se desea traducir a un código numérico.

    Returns:
        list: Una lista que contiene el código numérico correspondiente al mensaje de error.
        
    Notes:
        - El código 500 se utiliza para errores desconocidos que no están en el diccionario de excepciones.
        - Los códigos numéricos y mensajes de error son definidos en el diccionario `exception` y corresponden a distintos errores específicos que pueden ocurrir durante la ejecución del programa.
"""