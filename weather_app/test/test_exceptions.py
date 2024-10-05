import pytest
import os
from utils.obtenervuelos import obtener_vuelosPorIATA
from utils import obtenervuelos
from utils.obtenerclimas import obtener_coordenadas


@pytest.mark.exceptions
def test_obtener_coordenadas_invalid_input():
    with pytest.raises(Exception, match="Por favor, selecciona un lugar válido"):
        obtener_coordenadas("")
    with pytest.raises(Exception, match="Por favor, selecciona un lugar válido"):
        obtener_coordenadas(None)


@pytest.mark.exceptions
def test_cache_not_found(monkeypatch):
    def mock_abspath(path):
        return "ruta_inexistente/vuelos_cache.json"

    def mock_verificaEnCacheIATA(ruta, iata):
        return None  

    monkeypatch.setattr(os.path, 'abspath', mock_abspath)
    monkeypatch.setattr(obtenervuelos, 'verificaEnCacheIATA', mock_verificaEnCacheIATA)  

    resultado = obtener_vuelosPorIATA("MEX")
    assert resultado is None, "La función no manejó correctamente la falta de caché o datos"


@pytest.mark.exceptions
def test_iata_with_spaces(monkeypatch):
    def mock_verificaEnCacheIATA(ruta, iata):
        assert iata == "MEX", "La función no eliminó correctamente los espacios en blanco"
        return {"Vuelo": "MX123"}  

    monkeypatch.setattr(obtenervuelos, 'verificaEnCacheIATA', mock_verificaEnCacheIATA)  

    resultado = obtener_vuelosPorIATA(" MEX ")
    assert resultado == {"Vuelo": "MX123"}, "No manejó correctamente el IATA con espacios en blanco"

"""
Este conjunto de pruebas está enfocado en manejar excepciones y casos atípicos relacionados con la función `obtener_vuelosPorIATA` y otros componentes del sistema de vuelos. Cada test está etiquetado con `@pytest.mark.exceptions`, lo que permite agruparlos bajo un conjunto específico de pruebas de manejo de excepciones.

Tests incluidos:

1. `test_obtener_coordenadas_invalid_input`: 
   - Verifica que la función `obtener_coordenadas` arroje una excepción adecuada cuando se le pasa una entrada inválida, como una cadena vacía o `None`. Esto asegura que la función maneje correctamente entradas no válidas o faltantes.

2. `test_cache_not_found`: 
   - Utilizando `monkeypatch`, se simula un entorno en el que la ruta del archivo de caché no existe y `verificaEnCacheIATA` no encuentra datos. El test verifica que `obtener_vuelosPorIATA` maneje correctamente la falta de caché o datos, retornando `None` en lugar de fallar.

3. `test_iata_with_spaces`: 
   - Se prueba que la función `obtener_vuelosPorIATA` maneje correctamente códigos IATA con espacios en blanco antes y después. Utilizando `monkeypatch`, el test simula una respuesta correcta del caché, asegurándose de que los espacios en blanco se eliminen correctamente.

Cada test asegura que la lógica de manejo de errores y casos atípicos funcione correctamente, mejorando la robustez del sistema frente a entradas no esperadas o situaciones anómalas.
"""