
def traducirExcepción(msg):

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
        "Error en la solicitud de la API: 502": "302",  
        "Error en la solicitud de la API: 503": "303",  
        
    }

    for key, value in exception:

        if key == msg:
            return [value]
    
    return ["500"] 

"""
    Traduce un mensaje de error a un código de excepción correspondiente.

    Args:
        msg (str): El mensaje de error que se desea traducir.

    Returns:
        list: Una lista con el código de excepción correspondiente. Si no se encuentra el mensaje,
        devuelve el código "500" para un error desconocido.
"""  