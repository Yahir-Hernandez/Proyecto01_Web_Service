
from datetime import datetime, timedelta, timezone

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
    
    # Convertir de nuevo el objeto datetime a string en el formato solicitado
    return fecha_hora_redondeada.strftime("%Y-%m-%d %H:%M:%S")

    
def convertir_hora(hora):

    # Convertir la cadena a un objeto datetime en UTC
    utc = datetime.strptime(hora, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    
    # Restar 6 horas para convertir a CST
    cst = timezone(timedelta(hours=-6))
    horaSCT = utc.astimezone(cst)
    
    # Convertir de nuevo el objeto datetime a string en el formato solicitado
    return horaSCT.strftime("%Y-%m-%d %H:%M:%S")