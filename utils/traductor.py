from deep_translator import GoogleTranslator

#Corrige datos en ingles

def traducir_descripcion(descripcion):
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
        "clear sky": "cielo despejado",
        "few clouds": "pocas nubes",
        "scattered clouds": "nubes dispersas",
        "broken clouds": "nubes rasgadas",
        "overcast clouds": "cielo nuboso",
        "shower rain": "lluvia en chubascos",
        "rain": "lluvia",
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