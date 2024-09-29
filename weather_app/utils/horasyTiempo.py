
from datetime import datetime, timedelta, timezone
import pytz

cst = pytz.timezone('America/Chicago')

   
def redondea_hora(fechaHora):
    newfecha = datetime.fromisoformat(fechaHora.replace("Z", "+00:00"))

    minutos = newfecha.minute
    
    if minutos < 30:
        fredondeada = newfecha.replace(minute=0, second=0, microsecond=0)
    else:
        fredondeada = (newfecha + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
    
    return fredondeada.strftime("%Y-%m-%d %H:%M:%S")
"""
    Redondea la hora a la hora en punto más cercana dependiendo de los minutos.

    Args:
        fecha_hora_str (str): un string del tipo "2024-08-27T05:25:00+00:00" a redondear.

    Returns:
        str: Un string con la fecha y la hora redondeada.
"""

    
def convertir_hora(hora):

    utc = datetime.strptime(hora, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    
    cst = timezone(timedelta(hours=-6))
    horaSCT = utc.astimezone(cst)
    
    return horaSCT.strftime("%Y-%m-%d %H:%M:%S")

def ayer():
    """
    Devuelve el timestamp correspondiente a las 12:00 del mediodía del día anterior en formato UTC.

    Returns:
        int: Timestamp en formato UTC correspondiente a las 12:00 del día anterior.
    """
    ayer = datetime.now() - timedelta(days=1)
    inicio_ayer = cst.localize(ayer.replace(hour=0, minute=0, second=0, microsecond=0))
    return inicio_ayer.strftime("%Y-%m-%d %H:%M:%S")

def timestamp(fecha):

    fecha = datetime.fromisoformat(fecha)
    return int(fecha.timestamp())

def hoy():
    """
    Devuelve la fecha actual en formato 'YYYY-MM-DD'.

    Returns:
        str: Fecha actual en formato 'YYYY-MM-DD'.
    """
    hoy = datetime.now()
    return hoy.strftime("%Y-%m-%d %H:%M:%S")

def convertDT_a_CST(dt):
    '''Convierte una fecha de codigo dt a fecha cst enformato año-mes-dia 
    hora-minuto-segundo
    '''
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


def formato_dia_mes(fecha):
    """
    Devuelve la fecha en formato "dia/Mes".

    :param fecha: Objeto datetime o cadena con la fecha.
    :param formato: Formato de la cadena de fecha si 'fecha' es una cadena.
    :return: Cadena en formato "Año/Mes".
    """
    fech = datetime.fromisoformat(fecha)

    return fech.strftime("%d/%m")