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
Este conjunto de pruebas verifica la correcta gestión de excepciones y casos especiales en las funciones relacionadas con la obtención de vuelos y coordenadas.

Marcadas con `@pytest.mark.exceptions`:

- `test_obtener_coordenadas_invalid_input`: 
    - Verifica que la función `obtener_coordenadas` lance una excepción adecuada cuando se le proporciona una entrada no válida, como una cadena vacía o `None`.
    - Se espera que se lance una excepción con el mensaje "Por favor, selecciona un lugar válido".

- `test_cache_not_found`: 
    - Utilizando `monkeypatch`, simula una ruta de archivo inexistente para comprobar cómo se comporta la función `obtener_vuelosPorIATA` cuando no puede encontrar el archivo de caché.
    - La prueba se asegura de que, en caso de no encontrar datos en el caché, la función retorne `None` sin lanzar excepciones inesperadas.

- `test_iata_with_spaces`: 
    - Esta prueba verifica que la función `obtener_vuelosPorIATA` maneje correctamente los códigos IATA que contienen espacios en blanco.
    - Utiliza `monkeypatch` para reemplazar la función `verificaEnCacheIATA` y asegurarse de que el código IATA ingresado con espacios sea limpiado correctamente antes de la consulta.
    - Se comprueba que el código IATA " MEX " se procese correctamente y retorne los datos esperados.

Estas pruebas aseguran que las funciones manejen adecuadamente entradas no válidas, la falta de caché, y formatos incorrectos en los códigos IATA.
"""