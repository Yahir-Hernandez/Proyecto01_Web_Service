import pytest
import os
import sys

import utils.traductor import traducirExcepcion

@pytest.mark.traductor
def test_traducir_excepcion_valido():
    # Probar mensajes válidos
    assert traducirExcepcion("Por favor selecciona un lugar válido para solicitar el clima.") == ["101"]
    assert traducirExcepcion("No se pudo leer o no existe el archivo SCV dataset.") == ["102"]
    assert traducirExcepcion("Error en la solicitud de la API: 404") == ["204"]

@pytest.mark.traductor
def test_traducir_excepcion_invalido():
    # Probar un mensaje que no está en el diccionario
    assert traducirExcepcion("Mensaje desconocido") == ["500"]

@pytest.mark.traductor
def test_traducir_excepcion_no_iata():
    # Probar un mensaje específico
    assert traducirExcepcion("No se encontró el IATA.") == ["109"]

@pytest.mark.traductor
def test_traducir_excepcion_error_api_500():
    # Probar un error de API
    assert traducirExcepcion("Error en la solicitud de la API: 500") == ["300"]