import sys
import os
import pytest
from prediccion import predicc

# Añadir la ruta del módulo para que Python pueda encontrarlo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_prediccion_con_codigo_iata():
    # Test para el código IATA MEX
    assert predicc("MEX") == "Ciudad de México"

def test_prediccion_con_ciudad_tijuana():
    # Test para la ciudad Tijuana
    assert predicc("Tojuana") == "Tijuana"

def test_prediccion_con_ciudad_toluca():
    # Test para la ciudad Toluca
    assert predicc("THoluca") == "Toluca"

def test_prediccion_con_ciudad_con_error_tipografico():
    # Test para una ciudad con error tipográfico
    assert predicc("Guadalajra") == "Guadalajara"

