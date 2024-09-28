
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

"""
Esta prueba verifica el correcto funcionamiento de las funciones `reescribe_hora` y `convertir_hora`, las cuales manipulan y ajustan el formato de una fecha en UTC.

- `test_horas_1`: 
    - La prueba toma una fecha en formato UTC `"2024-08-27T05:25:00+00:00"`, y la función `reescribe_hora` se encarga de modificar la hora, ajustándola a un formato con minutos en cero, es decir, a las 05:00:00.
    - La prueba imprime el resultado modificado y luego verifica que el resultado de la función sea `"2024-08-27 05:00:00+00:00"`.
    - Finalmente, también se imprime el resultado de la función `convertir_hora`, que convierte el formato modificado de la hora para su posterior uso.

Estas funciones se utilizan para ajustar y convertir formatos de horas, asegurando que los datos estén en el formato correcto para ser procesados o mostrados.
"""