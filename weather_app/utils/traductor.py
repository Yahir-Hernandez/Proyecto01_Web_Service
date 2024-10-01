from deep_translator import GoogleTranslator

def traducir(descripcion):

    traduccion = GoogleTranslator(source='en', target='es').translate(descripcion)
    return traduccion

"""
    Traduce un texto en inglés al español utilizando Google Translator.

    Esta función utiliza la biblioteca GoogleTranslator para traducir un texto
    de inglés a español. Si la traducción se realiza correctamente, se devuelve
    el texto traducido.

    Args:
        descripcion (str): Texto en inglés que se desea traducir.

    Returns:
        str: Texto traducido al español.
"""

def traducir_main(clima_id):

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

"""
    Devuelve la descripción del clima correspondiente a un código de condición meteorológica.

    Esta función utiliza un diccionario predefinido que mapea códigos de clima
    a descripciones en español. Si el código proporcionado no se encuentra en el 
    diccionario, se devuelve una descripción predeterminada.

    Args:
        clima_id (int): Código de condición meteorológica.

    Returns:
        str: Descripción del clima en español correspondiente al código.
"""


def traducir_descripcion(descripcion_clima):

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
        "fog": "niebla",
        "sand": "arena",
        "dust": "polvo",
        "ash": "ceniza",
        "squall": "ráfaga",
        "tornado": "tornado"
    }
    return traducciones_descripcion.get(descripcion_clima, descripcion_clima)

"""
    Traduce la descripción detallada del clima del inglés al español.

    Esta función toma una descripción en inglés del clima y busca su traducción
    en un diccionario predefinido. Si no se encuentra una traducción, se devuelve
    la descripción original.

    Args:
        descripcion_clima (str): Descripción del clima en inglés (e.g., "clear sky").

    Returns:
        str: Descripción del clima en español.
"""


def traducirExcepcion(msg):

    exception ={

        "Por favor selecciona un lugar válido para solicitar el clima." : "101", 
        "No se pudo leer o no existe el archivo SCV dataset.": "102", 
        "Selecciona un origen o destino válidos." : "103", 
        "La ciudad de origen o destino debe de ser la Ciudad de México.": "104", 
        "La ciudad de origen y destino deben ser distintas." : "105", 
        "Por favor selecciona un iata válido." : "106", 
        "No se encontraron coincidencias para esa ciudad." : "107", 
        "No se pudo leer o no existe el archivo CSV IATAS." : "108",
        "No se encontró el IATA." : "109", 
        "Error en la solicitud de la API: 400": "200",  
        "Error en la solicitud de la API: 401": "201",  
        "Error en la solicitud de la API: 403": "203",
        "Error en la solicitud de la API: 404": "204",  
        "Error en la solicitud de la API: 500": "300",  
        "Error en la solicitud de la API: 502": "302", 
        "Error en la solicitud de la API: 503": "303",  
        
    }

    for key, value in exception.items():
        if key in msg:
            return [value, msg]
    
    return ["500", "error desconocido"] 
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