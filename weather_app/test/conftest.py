
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
    Función que modifica el resumen de la salida de Pytest mostrando información adicional sobre los tests categorizados por marcas específicas.

    Parámetros:
    - terminalreporter: Proporciona el objeto de reporter de pytest que contiene la información de los resultados de las pruebas.
    - exitstatus: El estado de salida que indica si pytest se completó correctamente o con fallos.
    - config: La configuración de pytest en uso.

    Detalles:
    Esta función extiende el reporte estándar de pytest al final de las ejecuciones de pruebas, 
    proporcionando un resumen categorizado por las marcas `iatas`, `correccion`, y `exceptions`. 
    Además de mostrar el total de tests ejecutados bajo cada marca, también calcula cuántos pasaron, fallaron, 
    fueron omitidos y el porcentaje de éxito para cada categoría.

    Funciones Internas:
    - count_tests_by_mark(mark): 
        Calcula y devuelve el total de tests, el número de tests pasados, fallidos, omitidos y el porcentaje de éxito para una marca específica.
        
    Uso de la función:
    La función se llama automáticamente al final de una ejecución de pytest para personalizar el informe de resultados.
"""