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
Este conjunto de pruebas tiene como propósito validar el comportamiento de la función `predicc`, la cual está diseñada para corregir errores tipográficos o proporcionar predicciones basadas en nombres de ciudades y códigos IATA. Las pruebas están organizadas bajo dos categorías principales: aquellas que verifican la predicción con código IATA o nombres de ciudades (marcadas con `@pytest.mark.iatas`) y aquellas que validan correcciones de errores tipográficos o manejo de mayúsculas (marcadas con `@pytest.mark.correccion`).

1. En `test_prediccion_con_codigo_iata`, se verifica que la función `predicc` sea capaz de asociar correctamente el código IATA "MEX" con la ciudad "Ciudad de México".

2. La prueba `test_prediccion_con_ciudad_tijuana` asegura que la función pueda corregir un error en el nombre de la ciudad "Tojuana" y devolver la predicción correcta: "Tijuana".

3. En `test_prediccion_con_ciudad_toluca`, se valida que la función maneje adecuadamente un error tipográfico más complejo en el nombre "THoluca", devolviendo "Toluca" como la ciudad correcta.

4. Las pruebas marcadas como `@pytest.mark.correccion` están diseñadas para validar el comportamiento de la función ante errores tipográficos y diferentes formatos:
   - En `test_prediccion_con_ciudad_con_error_tipografico`, se verifica que un error en la ciudad "Guadalajra" sea corregido correctamente a "Guadalajara".
   - `test_prediccion_bajo_umbral` comprueba que cuando se ingresa una cadena con baja similitud, como "Xylophone", la función levante una excepción de tipo `ValueError` al no encontrar una coincidencia suficientemente cercana.
   - Finalmente, `test_prediccion_con_mayusculas` valida que la función maneje correctamente entradas en mayúsculas, retornando "Tijuana" cuando se ingresa "TIJUANA".

Estas pruebas aseguran que la función `predicc` funcione de manera robusta, proporcionando correcciones precisas y manejando errores comunes en las entradas, tanto en nombres de ciudades como en códigos IATA.
"""