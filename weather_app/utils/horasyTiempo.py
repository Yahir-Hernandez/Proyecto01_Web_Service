
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

"""
    Convierte una cadena de fecha y hora en formato UTC a la hora en la zona horaria CST (Central Standard Time).
    
    Args:
        hora (str): Fecha y hora en formato "YYYY-MM-DD HH:MM:SS" en UTC.

    Returns:
        str: Fecha y hora en formato "YYYY-MM-DD HH:MM:SS" en CST.
"""

def ayer():

    ayer = datetime.now() - timedelta(days=1)
    inicio_ayer = cst.localize(ayer.replace(hour=0, minute=0, second=0, microsecond=0))
    return inicio_ayer.strftime("%Y-%m-%d %H:%M:%S")

"""
    Obtiene la fecha y hora del inicio del día anterior en la zona horaria CST.
    
    Args:
        None

    Returns:
        str: Fecha y hora del inicio del día anterior en formato "YYYY-MM-DD HH:MM:SS".
"""

def timestamp(fecha):

    fecha = datetime.fromisoformat(fecha)
    return int(fecha.timestamp())

"""
    Convierte una fecha en formato ISO a un timestamp Unix (segundos desde la época).
    
    Args:
        fecha (str): Fecha en formato ISO (ej. "YYYY-MM-DD HH:MM:SS").

    Returns:
        int: Timestamp Unix correspondiente a la fecha.
"""

def hoy():

    hoy = datetime.now()
    return hoy.strftime("%Y-%m-%d %H:%M:%S")

"""
    Obtiene la fecha y hora actuales en formato "YYYY-MM-DD HH:MM:SS".
    
    Args:
        None

    Returns:
        str: Fecha y hora actuales en formato "YYYY-MM-DD HH:MM:SS".
"""

def convertDT_a_CST(dt):

    return datetime.fromtimestamp(dt, cst).strftime('%Y-%m-%d %H:%M:%S')

"""
    Convierte un timestamp Unix a una cadena de fecha y hora en la zona horaria CST.
    
    Args:
        dt (int): Timestamp Unix a convertir.

    Returns:
        str: Fecha y hora en formato "YYYY-MM-DD HH:MM:SS" en CST.
"""

def formato_hora_minuto(fecha):
    
    fech = datetime.fromisoformat(fecha)

    return fech.strftime("%H:%M")

"""
    Formatea una fecha en formato ISO para devolver solo la hora y los minutos.
    
    Args:
        fecha (str): Fecha en formato ISO (ej. "YYYY-MM-DD HH:MM:SS").

    Returns:
        str: Hora y minutos en formato "HH:MM".
"""

def formato_dia_mes(fecha):

    fech = datetime.fromisoformat(fecha)

    return fech.strftime("%d/%m")

"""
    Formatea una fecha en formato ISO para devolver solo el día y el mes.
    
    Args:
        fecha (str): Fecha en formato ISO (ej. "YYYY-MM-DD HH:MM:SS").

    Returns:
        str: Día y mes en formato "DD/MM".
"""