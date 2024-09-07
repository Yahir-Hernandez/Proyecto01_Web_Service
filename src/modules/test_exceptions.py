import pytest
<<<<<<< Updated upstream:src/modules/test_exceptions.py
from obtenerclimas import weather, obtener_coordenadas  # Asegúrate de ajustar el nombre del módulo según tu estructura
import os
from obtenervuelos import obtener_vuelosPorIATA
=======
from services.obtenerclimas import weather, obtener_coordenadas 
from services.obtenervuelos import obtener_vuelosPorIATA
>>>>>>> Stashed changes:test/test_exceptions.py
#===============================================================Obtener cordenadas========================================================================================


@pytest.mark.exceptions
# Test para verificar que obtener_coordenadas lanza una excepción con una entrada vacía o inválida
def test_obtener_coordenadas_invalid_input():
    with pytest.raises(Exception, match="Por favor, selecciona un lugar válido"):
        obtener_coordenadas("")

    with pytest.raises(Exception, match="Por favor, selecciona un lugar válido"):
        obtener_coordenadas(None)

#===============================================================Obtener vuelos========================================================================================


@pytest.mark.exceptions
# 1. Prueba de caché no encontrado o vacío
def test_cache_not_found(monkeypatch):
    def mock_abspath(path):
        return "ruta_inexistente/vuelos_cache.json"
    
    def mock_verificaEnCacheIATA(ruta, iata):
        return None  # Simula que no se encuentra en caché

    monkeypatch.setattr(os.path, 'abspath', mock_abspath)
    monkeypatch.setattr('obtenervuelos.verificaEnCacheIATA', mock_verificaEnCacheIATA)
    
    resultado = obtener_vuelosPorIATA("MEX")
    assert resultado is None, "La función no manejó correctamente la falta de caché o datos"


@pytest.mark.exceptions
# Prueba de IATA con espacios extras
def test_iata_with_spaces(monkeypatch):
    def mock_verificaEnCacheIATA(ruta, iata):
        assert iata == "MEX", "La función no eliminó correctamente los espacios en blanco"
        return {"Vuelo": "MX123"}  # Simula un resultado

    monkeypatch.setattr('obtenervuelos.verificaEnCacheIATA', mock_verificaEnCacheIATA)
    
    resultado = obtener_vuelosPorIATA(" MEX ")
    assert resultado == {"Vuelo": "MX123"}, "No manejó correctamente el IATA con espacios en blanco"