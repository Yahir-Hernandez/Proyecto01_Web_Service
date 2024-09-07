import sys
import os
import pytest
# Añadir la ruta del módulo para que Python pueda encontrarlo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.predicc import predicc

@pytest.mark.iatas
def test_prediccion_con_codigo_iata():
    # Test para el código IATA MEX
    assert predicc("MEX") == "Ciudad de México"

@pytest.mark.iatas
def test_prediccion_con_ciudad_tijuana():
    # Test para la ciudad Tijuana
    assert predicc("Tojuana") == "Tijuana"

@pytest.mark.iatas
def test_prediccion_con_ciudad_toluca():
    # Test para la ciudad Toluca
    assert predicc("THoluca") == "Toluca"

@pytest.mark.correccion
def test_prediccion_con_ciudad_con_error_tipografico():
    # Test para una ciudad con error tipográfico
    assert predicc("Guadalajra") == "Guadalajara"

@pytest.mark.correccion
def test_prediccion_bajo_umbral():
    # Test para superar el 75% de parecido
    with pytest.raises(ValueError):
        predicc("Xylophone")

@pytest.mark.correccion
def test_prediccion_con_mayusculas():
    # Test para ver cómo se comporta con mayúsculas
    assert predicc("TIJUANA") == "Tijuana"