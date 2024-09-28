
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    
    total_tests = terminalreporter._numcollected
    
    def count_tests_by_mark(mark):
        passed = len([x for x in terminalreporter.stats.get('passed', []) if mark in x.keywords])
        failed = len([x for x in terminalreporter.stats.get('failed', []) if mark in x.keywords])
        skipped = len([x for x in terminalreporter.stats.get('skipped', []) if mark in x.keywords])
        total = passed + failed + skipped
        percentage_passed = (passed / total) * 100 if total else 0
        return total, passed, failed, skipped, percentage_passed

    total_iatas, passed_iatas, failed_iatas, skipped_iatas, percentage_iatas = count_tests_by_mark('iatas')
    
    total_correccion, passed_correccion, failed_correccion, skipped_correccion, percentage_correccion = count_tests_by_mark('correccion')

    total_exceptions, passed_exceptions, failed_exceptions, skipped_exceptions, percentage_exceptions = count_tests_by_mark('exceptions')
    

    terminalreporter.write_sep("=", "Resumen de tests por categoría")
    
    terminalreporter.write_sep("-", "Resumen de tests IATA")
    terminalreporter.write_line(f"Total de tests IATA: {total_iatas}")
    terminalreporter.write_line(f"Tests IATA pasados: {passed_iatas}")
    terminalreporter.write_line(f"Tests IATA fallidos: {failed_iatas}")
    terminalreporter.write_line(f"Tests IATA omitidos: {skipped_iatas}")
    terminalreporter.write_line(f"Porcentaje de éxito IATA: {percentage_iatas:.2f}%")
    
    terminalreporter.write_sep("-", "Resumen de tests Corrección")
    terminalreporter.write_line(f"Total de tests Corrección: {total_correccion}")
    terminalreporter.write_line(f"Tests Corrección pasados: {passed_correccion}")
    terminalreporter.write_line(f"Tests Corrección fallidos: {failed_correccion}")
    terminalreporter.write_line(f"Tests Corrección omitidos: {skipped_correccion}")
    terminalreporter.write_line(f"Porcentaje de éxito Corrección: {percentage_correccion:.2f}%")

    terminalreporter.write_sep("-", "Resumen de tests Exceptions")
    terminalreporter.write_line(f"Total de tests Exceptions: {total_exceptions}")
    terminalreporter.write_line(f"Tests Corrección pasados: {passed_exceptions}")
    terminalreporter.write_line(f"Tests Corrección fallidos: {failed_exceptions}")
    terminalreporter.write_line(f"Tests Corrección omitidos: {skipped_exceptions}")
    terminalreporter.write_line(f"Porcentaje de éxito Exceptions: {percentage_exceptions:.2f}%")

"""
Función `pytest_terminal_summary`:
Esta función se utiliza para personalizar el resumen de pruebas al final de la ejecución de pytest. Recoge los resultados de las pruebas y genera un informe categorizado por los siguientes marcadores: `iatas`, `correccion` y `exceptions`.

1. Recuento total de pruebas:
   - `total_tests`: Obtiene el número total de pruebas ejecutadas.

2. Función `count_tests_by_mark`:
   - Esta función cuenta las pruebas para cada marcador específico (`iatas`, `correccion`, `exceptions`) dividiendo las pruebas en pasadas, fallidas y omitidas.
   - Además, calcula el porcentaje de éxito para cada grupo de pruebas.

3. Estadísticas por categorías:
   - Para cada marcador, la función extrae las estadísticas:
     - Total de pruebas.
     - Número de pruebas pasadas.
     - Número de pruebas fallidas.
     - Número de pruebas omitidas.
     - Porcentaje de éxito (calculado como `(pruebas pasadas / total de pruebas) * 100`).

4. Informe en la terminal:
   - Se imprime un informe detallado que resume los resultados de las pruebas para cada categoría, utilizando separadores visuales para mejorar la legibilidad.
   - El informe incluye tanto el número total de pruebas como el porcentaje de éxito para cada categoría.

5. Categorías consideradas:
   - `iatas`: Pruebas relacionadas con la funcionalidad de IATA.
   - `correccion`: Pruebas que verifican la corrección automática de entradas erróneas.
   - `exceptions`: Pruebas que validan el manejo de excepciones y errores.
"""