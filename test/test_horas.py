#Test para probar la el modulo de fechas y hora
import pytest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.horasyTiempo import reescribe_hora, convertir_hora

def test_horas_1():
    fecha_UTC = "2024-08-27T05:25:00+00:00"
    print(reescribe_hora(fecha_UTC))
    assert reescribe_hora(fecha_UTC) == "2024-08-27 05:00:00+00:00"
    
fecha = "2024-08-27T05:25:00+00:00"
print(reescribe_hora(fecha))
print(convertir_hora(reescribe_hora(fecha)))