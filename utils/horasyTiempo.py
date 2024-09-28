
from datetime import datetime, timedelta, timezone
import pytz

# Configurar la zona horaria CST (Central Standard Time)
cst = pytz.timezone('America/Chicago')

   
def reescribe_hora(fecha_hora_str):
    #convierte una cadena en formato ISO 8601 (como "2024-08-27T05:25:00+00:00") a un objeto datetime de Python.
    fecha_hora = datetime.fromisoformat(fecha_hora_str.replace("Z", "+00:00"))

    # Extraer los minutos
    minutos = fecha_hora.minute
    
    # Redondear hacia la hora más cercana
    if minutos < 30:
        fecha_hora_redondeada = fecha_hora.replace(minute=0, second=0, microsecond=0)
    else:
        fecha_hora_redondeada = (fecha_hora + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
    
    return fecha_hora_redondeada.strftime("%Y-%m-%d %H:%M:%S")
"""
    Redondea la hora a la hora en punto más cercana dependiendo de los minutos.

    Args:
        fecha_hora_str (str): un string del tipo "2024-08-27T05:25:00+00:00" a redondear.

    Returns:
        str: Un string con la fecha y la hora redondeada.
"""

    
def convertir_hora(hora):

    # Convertir la cadena a un objeto datetime en UTC
    utc = datetime.strptime(hora, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    
    # Restar 6 horas para convertir a CST
    cst = timezone(timedelta(hours=-6))
    horaSCT = utc.astimezone(cst)
    
    # Convertir de nuevo el objeto datetime a string en el formato solicitado
    return horaSCT.strftime("%Y-%m-%d %H:%M:%S")

def ayer():
    """
    Devuelve el timestamp correspondiente a las 12:00 del mediodía del día anterior en formato UTC.

    Returns:
        int: Timestamp en formato UTC correspondiente a las 12:00 del día anterior.
    """
    ayer = datetime.now() - timedelta(days=1)
    
    inicio_del_dia_anterior = cst.localize(ayer.replace(hour=0, minute=0, second=0, microsecond=0))
    return int(inicio_del_dia_anterior.timestamp())

def fecha_final(fecha):
    '''
        Convierte la fecha proporcionada final del día en formato UTC y devuelve el timestamp correspondiente.

        Esta función toma una fecha en formato 'YYYY-MM-DD', la convierte al inicio del día en la zona horaria CST,
        la convierte a UTC y luego devuelve el valor en formato timestamp.

        Args:
            fecha (str): Fecha en formato 'YYYY-MM-DD'.

        Returns:
            int: Timestamp en formato UTC correspondiente al inicio del día.
    '''
    
    final_del_dia = cst.localize(datetime.strptime(fecha, "%Y-%m-%d").replace(hour=23, minute=59, second=59))
    return int(final_del_dia.timestamp())

def fecha_hoy():
    """
    Devuelve la fecha actual en formato 'YYYY-MM-DD'.

    Returns:
        str: Fecha actual en formato 'YYYY-MM-DD'.
    """
    hoy = datetime.now()

    return hoy.strftime('%Y-%m-%d')

def convertDT_a_CST(dt):
    '''Convierte una fecha de codigo dt a fecha cst enformato año-mes-dia hora-minuto-segundo'''
    return datetime.fromtimestamp(dt, cst).strftime('%Y-%m-%d %H:%M:%S')


def formato_hora_minuto(fecha):
    """
    Devuelve la fecha en formato "Hora-Minuto".

    :param fecha: Objeto datetime o cadena con la fecha.
    :param formato: Formato de la cadena de fecha si 'fecha' es una cadena.
    :return: Cadena en formato "Hora-Minuto".
    """
    fech = datetime.fromisoformat(fecha)

    return fech.strftime("%H:%M")


def formato_ano_mes(fecha):
    """
    Devuelve la fecha en formato "dia/Mes".

    :param fecha: Objeto datetime o cadena con la fecha.
    :param formato: Formato de la cadena de fecha si 'fecha' es una cadena.
    :return: Cadena en formato "Año/Mes".
    """
    fech = datetime.fromisoformat(fecha)

    return fech.strftime("%d/%m")


