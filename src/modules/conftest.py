
import pytest

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    # Obtener el número de tests totales, pasados, fallidos y omitidos
    total_tests = terminalreporter._numcollected
    
    def count_tests_by_mark(mark):
        passed = len([x for x in terminalreporter.stats.get('passed', []) if mark in x.keywords])
        failed = len([x for x in terminalreporter.stats.get('failed', []) if mark in x.keywords])
        skipped = len([x for x in terminalreporter.stats.get('skipped', []) if mark in x.keywords])
        total = passed + failed + skipped
        percentage_passed = (passed / total) * 100 if total else 0
        return total, passed, failed, skipped, percentage_passed

    # Resumen para los tests de iatas
    total_iatas, passed_iatas, failed_iatas, skipped_iatas, percentage_iatas = count_tests_by_mark('iatas')
    
    # Resumen para los tests de corrección
    total_correccion, passed_correccion, failed_correccion, skipped_correccion, percentage_correccion = count_tests_by_mark('correccion')
    
    # Mostrar los resultados generales
    terminalreporter.write_sep("=", "Resumen de tests por categoría")
    
    # Resumen de los tests IATA
    terminalreporter.write_sep("-", "Resumen de tests IATA")
    terminalreporter.write_line(f"Total de tests IATA: {total_iatas}")
    terminalreporter.write_line(f"Tests IATA pasados: {passed_iatas}")
    terminalreporter.write_line(f"Tests IATA fallidos: {failed_iatas}")
    terminalreporter.write_line(f"Tests IATA omitidos: {skipped_iatas}")
    terminalreporter.write_line(f"Porcentaje de éxito IATA: {percentage_iatas:.2f}%")
    
    # Resumen de los tests de corrección
    terminalreporter.write_sep("-", "Resumen de tests Corrección")
    terminalreporter.write_line(f"Total de tests Corrección: {total_correccion}")
    terminalreporter.write_line(f"Tests Corrección pasados: {passed_correccion}")
    terminalreporter.write_line(f"Tests Corrección fallidos: {failed_correccion}")
    terminalreporter.write_line(f"Tests Corrección omitidos: {skipped_correccion}")
    terminalreporter.write_line(f"Porcentaje de éxito Corrección: {percentage_correccion:.2f}%")