import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.predicc import predicc

@pytest.mark.iatas
def test_prediccion_con_codigo_iata():
    assert predicc("MEX") == "Ciudad de México"

@pytest.mark.iatas
def test_prediccion_con_ciudad_tijuana():
    assert predicc("Tojuana") == "Tijuana"

@pytest.mark.iatas
def test_prediccion_con_ciudad_toluca():
    assert predicc("THoluca") == "Toluca"

@pytest.mark.correccion
def test_prediccion_con_ciudad_con_error_tipografico():
    assert predicc("Guadalajra") == "Guadalajara"

@pytest.mark.correccion
def test_prediccion_bajo_umbral():
    with pytest.raises(ValueError):
        predicc("Xylophone")

@pytest.mark.correccion
def test_prediccion_con_mayusculas():
    assert predicc("TIJUANA") == "Tijuana"

"""
Este conjunto de pruebas está diseñado para verificar la funcionalidad de la función `predicc`, la cual intenta predecir el nombre correcto de una ciudad basado en una entrada proporcionada por el usuario, utilizando una lista de ciudades y un umbral de similitud.

Las pruebas están organizadas en dos conjuntos, diferenciados por los marcadores `@pytest.mark.iatas` y `@pytest.mark.correccion`:

Marcador `@pytest.mark.iatas`:
- `test_prediccion_con_codigo_iata`: Verifica que un código IATA válido devuelva la ciudad correspondiente.
- `test_prediccion_con_ciudad_tijuana`: Prueba la predicción de "Tijuana" con un error tipográfico ("Tojuana").
- `test_prediccion_con_ciudad_toluca`: Prueba la predicción de "Toluca" con un error tipográfico ("THoluca").

Marcador `@pytest.mark.correccion`:
- `test_prediccion_con_ciudad_con_error_tipografico`: Verifica que un error tipográfico en el nombre de la ciudad, como "Guadalajra", sea corregido a "Guadalajara".
- `test_prediccion_bajo_umbral`: Verifica que se lance una excepción cuando la ciudad ingresada ("Xylophone") no tiene suficientes coincidencias según el umbral de similitud.
- `test_prediccion_con_mayusculas`: Verifica que una entrada en mayúsculas ("TIJUANA") sea correctamente predicha como "Tijuana".

Estas pruebas aseguran que la función `predicc` maneje errores tipográficos menores y entradas en mayúsculas, y que sea capaz de identificar cuando no se puede hacer una predicción válida bajo un umbral definido.
"""