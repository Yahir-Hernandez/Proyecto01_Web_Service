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
        return None  # Simula que no se encuentra en caché

    monkeypatch.setattr(os.path, 'abspath', mock_abspath)
    monkeypatch.setattr(obtenervuelos, 'verificaEnCacheIATA', mock_verificaEnCacheIATA)  # Corregido

    resultado = obtener_vuelosPorIATA("MEX")
    assert resultado is None, "La función no manejó correctamente la falta de caché o datos"


@pytest.mark.exceptions
def test_iata_with_spaces(monkeypatch):
    def mock_verificaEnCacheIATA(ruta, iata):
        assert iata == "MEX", "La función no eliminó correctamente los espacios en blanco"
        return {"Vuelo": "MX123"}  # Simula un resultado

    monkeypatch.setattr(obtenervuelos, 'verificaEnCacheIATA', mock_verificaEnCacheIATA)  # Corregido

    resultado = obtener_vuelosPorIATA(" MEX ")
    assert resultado == {"Vuelo": "MX123"}, "No manejó correctamente el IATA con espacios en blanco"
