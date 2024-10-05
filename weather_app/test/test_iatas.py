import pytest
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.iatas import iatasC

@pytest.mark.iatas
def test_iatasC_toluca():
    assert iatasC("Toluca") == "TLC"

@pytest.mark.iatas
def test_iatasC_monterrey():
    assert iatasC("Monterrey") == "MTY"

@pytest.mark.iatas
def test_iatasC_ciudad_de_mexico():
    assert iatasC("Ciudad de México") == "MEX"

@pytest.mark.iatas
def test_iatasC_tampico():
    assert iatasC("Tampico") == "TAM"

@pytest.mark.iatas
def test_iatasC_guadalajara():
    assert iatasC("Guadalajara") == "GDL"

@pytest.mark.iatas
def test_iatasC_ciudad_juarez():
    assert iatasC("Ciudad Juárez") == "CJS"

@pytest.mark.iatas
def test_iatasC_cancun():
    assert iatasC("Cancún") == "CUN"

@pytest.mark.iatas
def test_iatasC_tijuana():
    assert iatasC("Tijuana") == "TIJ"

@pytest.mark.iatas
def test_iatasC_hermosillo():
    assert iatasC("Hermosillo") == "HMO"

@pytest.mark.iatas
def test_iatasC_ciudad_del_carmen():
    assert iatasC("Ciudad del Carmen") == "CME"

@pytest.mark.iatas
def test_iatasC_merida():
    assert iatasC("Mérida") == "MID"

@pytest.mark.iatas
def test_iatasC_chetumal():
    assert iatasC("Chetumal") == "CTM"

@pytest.mark.iatas
def test_iatasC_veracruz():
    assert iatasC("Veracruz") == "VER"

@pytest.mark.iatas
def test_iatasC_oaxaca():
    assert iatasC("Oaxaca") == "OAX"

@pytest.mark.iatas
def test_iatasC_huatulco():
    assert iatasC("Huatulco") == "HUX"

@pytest.mark.iatas
def test_iatasC_puerto_vallarta():
    assert iatasC("Puerto Vallarta") == "PVR"

@pytest.mark.iatas
def test_iatasC_puerto_escondido():
    assert iatasC("Puerto Escondido") == "PXM"

@pytest.mark.iatas
def test_iatasC_acapulco():
    assert iatasC("Acapulco") == "ACA"

@pytest.mark.iatas
def test_iatasC_ixtapa_zihuatanejo():
    assert iatasC("Ixtapa-Zihuatanejo") == "ZIH"

@pytest.mark.iatas
def test_iatasC_aguascalientes():
    assert iatasC("Aguascalientes") == "AGU"

@pytest.mark.iatas
def test_iatasC_villahermosa():
    assert iatasC("Villahermosa") == "VSA"

@pytest.mark.iatas
def test_iatasC_cozumel():
    assert iatasC("Cozumel") == "CZM"

@pytest.mark.iatas
def test_iatasC_chihuahua():
    assert iatasC("Chihuahua") == "CUU"

@pytest.mark.iatas
def test_iatasC_torreon():
    assert iatasC("Torreón") == "TRC"

@pytest.mark.iatas
def test_iatasC_queretaro():
    assert iatasC("Querétaro") == "QRO"

@pytest.mark.iatas
def test_iatasC_guanajuato():
    assert iatasC("Guanajuato") == "BJX"

@pytest.mark.iatas
def test_iatasC_puebla():
    assert iatasC("Puebla") == "PBC"

@pytest.mark.iatas
def test_iatasC_san_luis_potosi():
    assert iatasC("San Luis Potosí") == "SLP"

@pytest.mark.iatas
def test_iatasC_zacatecas():
    assert iatasC("Zacatecas") == "ZCL"

@pytest.mark.iatas
def test_iatasC_lima():
    assert iatasC("Lima") == "LIM"

@pytest.mark.iatas
def test_iatasC_la_habana():
    assert iatasC("La Habana") == "HAV"

@pytest.mark.iatas
def test_iatasC_bogota():
    assert iatasC("Bogotá") == "BOG"

@pytest.mark.iatas
def test_iatasC_miami():
    assert iatasC("Miami") == "MIA"

@pytest.mark.iatas
def test_iatasC_los_angeles():
    assert iatasC("Los Ángeles") == "LAX"

@pytest.mark.iatas
def test_iatasC_nueva_york():
    assert iatasC("Nueva York") == "JFK"

@pytest.mark.iatas
def test_iatasC_mazatlan():
    assert iatasC("Mazatlán") == "MZT"

@pytest.mark.iatas
def test_iatasC_ciudad_de_guatemala():
    assert iatasC("Ciudad de Guatemala") == "GUA"

@pytest.mark.iatas
def test_iatasC_belice():
    assert iatasC("Belice") == "BZE"

@pytest.mark.iatas
def test_iatasC_dallas_fort_worth():
    assert iatasC("Dallas/Fort Worth") == "DFW"

@pytest.mark.iatas
def test_iatasC_chicago():
    assert iatasC("Chicago") == "ORD"

@pytest.mark.iatas
def test_iatasC_phoenix():
    assert iatasC("Phoenix") == "PHX"

@pytest.mark.iatas
def test_iatasC_filadelfia():
    assert iatasC("Filadelfia") == "PHL"

@pytest.mark.iatas
def test_iatasC_charlotte():
    assert iatasC("Charlotte") == "CLT"

@pytest.mark.iatas
def test_iatasC_toronto():
    assert iatasC("Toronto") == "YYZ"

@pytest.mark.iatas
def test_iatasC_houston():
    assert iatasC("Houston") == "IAH"

@pytest.mark.iatas
def test_iatasC_vancouver():
    assert iatasC("Vancouver") == "YVR"

@pytest.mark.iatas
def test_iatasC_paris():
    assert iatasC("París") == "CDG"

@pytest.mark.iatas
def test_iatasC_amsterdam():
    assert iatasC("Ámsterdam") == "AMS"

@pytest.mark.iatas
def test_iatasC_atlanta():
    assert iatasC("Atlanta") == "ATL"

@pytest.mark.iatas
def test_iatasC_ciudad_obregon():
    assert iatasC("Ciudad Obregón") == "CEN"

@pytest.mark.iatas
def test_iatasC_madrid():
    assert iatasC("Madrid") == "MAD"

@pytest.mark.iatas
def test_iatasC_santiago_de_chile():
    assert iatasC("Santiago de Chile") == "SCL"

@pytest.mark.iatas
def test_iatasC_austin():
    assert iatasC("Austin") == "AUS"

@pytest.mark.iatas
def test_iatasC_buenos_aires():
    assert iatasC("Buenos Aires") == "EZE"

@pytest.mark.iatas
def test_iatasC_boston():
    assert iatasC("Boston") == "BOS"

@pytest.mark.iatas
def test_iatasC_campeche():
    assert iatasC("Campeche") == "CPE"

@pytest.mark.iatas
def test_iatasC_culiacan():
    assert iatasC("Culiacán") == "CUL"

@pytest.mark.iatas
def test_iatasC_denver():
    assert iatasC("Denver") == "DEN"

@pytest.mark.iatas
def test_iatasC_detroit():
    assert iatasC("Detroit") == "DTW"

@pytest.mark.iatas
def test_iatasC_dubai():
    assert iatasC("Dubái") == "DXB"

@pytest.mark.iatas
def test_iatasC_durango():
    assert iatasC("Durango") == "DGO"

@pytest.mark.iatas
def test_iatasC_estambul():
    assert iatasC("Estambul") == "IST"

@pytest.mark.iatas
def test_iatasC_frankfurt():
    assert iatasC("Frankfurt") == "FRA"

@pytest.mark.iatas
def test_iatasC_la_paz():
    assert iatasC("La Paz") == "LAP"

@pytest.mark.iatas
def test_iatasC_las_vegas():
    assert iatasC("Las Vegas") == "LAS"

@pytest.mark.iatas
def test_iatasC_leon_bajio():
    assert iatasC("León/Bajío") == "BJX"

@pytest.mark.iatas
def test_iatasC_los_mochis():
    assert iatasC("Los Mochis") == "LMM"

@pytest.mark.iatas
def test_iatasC_managua():
    assert iatasC("Managua") == "MGA"

@pytest.mark.iatas
def test_iatasC_manzanillo():
    assert iatasC("Manzanillo") == "ZLO"

@pytest.mark.iatas
def test_iatasC_matamoros():
    assert iatasC("Matamoros") == "MAM"

@pytest.mark.iatas
def test_iatasC_medellin():
    assert iatasC("Medellín") == "MDE"

@pytest.mark.iatas
def test_iatasC_mexicali():
    assert iatasC("Mexicali") == "MXL"

@pytest.mark.iatas
def test_iatasC_minatitlan():
    assert iatasC("Minatitlán") == "MTT"

@pytest.mark.iatas
def test_iatasC_minneapolis():
    assert iatasC("Minneapolis") == "MSP"

@pytest.mark.iatas
def test_iatasC_montreal():
    assert iatasC("Montreal") == "YUL"

@pytest.mark.iatas
def test_iatasC_newark():
    assert iatasC("Newark") == "EWR"

@pytest.mark.iatas
def test_iatasC_nuevo_laredo():
    assert iatasC("Nuevo Laredo") == "NLD"

@pytest.mark.iatas
def test_iatasC_oakland():
    assert iatasC("Oakland") == "OAK"

@pytest.mark.iatas
def test_iatasC_orlando():
    assert iatasC("Orlando") == "MCO"

@pytest.mark.iatas
def test_iatasC_panama():
    assert iatasC("Panamá") == "PTY"

@pytest.mark.iatas
def test_iatasC_raleigh():
    assert iatasC("Raleigh") == "RDU"

@pytest.mark.iatas
def test_iatasC_reynosa():
    assert iatasC("Reynosa") == "REX"

@pytest.mark.iatas
def test_iatasC_roma():
    assert iatasC("Roma") == "FCO"

@pytest.mark.iatas
def test_iatasC_san_antonio():
    assert iatasC("San Antonio") == "SAT"

@pytest.mark.iatas
def test_iatasC_san_francisco():
    assert iatasC("San Francisco") == "SFO"

@pytest.mark.iatas
def test_iatasC_san_salvador():
    assert iatasC("San Salvador") == "SAL"

@pytest.mark.iatas
def test_iatasC_salt_lake_city():
    assert iatasC("Salt Lake City") == "SLC"

@pytest.mark.iatas
def test_iatasC_san_jose():
    assert iatasC("San José") == "SJO"

@pytest.mark.iatas
def test_iatasC_sao_paulo():
    assert iatasC("São Paulo") == "GRU"

@pytest.mark.iatas
def test_iatasC_seattle():
    assert iatasC("Seattle") == "SEA"

@pytest.mark.iatas
def test_iatasC_seul():
    assert iatasC("Seúl") == "ICN"

@pytest.mark.iatas
def test_iatasC_shenzhen():
    assert iatasC("Shenzhen") == "SZX"

@pytest.mark.iatas
def test_iatasC_san_jose_del_cabo():
    assert iatasC("San José del Cabo") == "SJD"

@pytest.mark.iatas
def test_iatasC_santo_domingo():
    assert iatasC("Santo Domingo") == "SDQ"

@pytest.mark.iatas
def test_iatasC_tampa():
    assert iatasC("Tampa") == "TPA"

@pytest.mark.iatas
def test_iatasC_tapachula():
    assert iatasC("Tapachula") == "TAP"

@pytest.mark.iatas
def test_iatasC_tepic():
    assert iatasC("Tepic") == "TPQ"

@pytest.mark.iatas
def test_iatasC_tokio():
    assert iatasC("Tokio") == "NRT"

@pytest.mark.iatas
def test_iatasC_tuxtla_gutierrez():
    assert iatasC("Tuxtla Gutiérrez") == "TGZ"

@pytest.mark.iatas
def test_iatasC_washington_dc():
    assert iatasC("Washington D.C.") == "DCA"

"""
Este conjunto de pruebas tiene como objetivo validar el correcto funcionamiento de la función `iatasC`, la cual se encarga de asignar los códigos IATA correctos a ciudades específicas. La etiqueta `@pytest.mark.iatas` permite agrupar las pruebas relacionadas con la asignación de códigos IATA, facilitando la ejecución y organización de este tipo de tests.

Cada prueba se centra en una ciudad en particular, verificando que el código IATA retornado por la función coincida con el esperado:

Estas pruebas son fundamentales para asegurar la precisión de la función `iatasC`, garantizando que cada ciudad esté correctamente asociada a su código IATA correspondiente, lo cual es crucial para aplicaciones que dependan de datos de transporte aéreo o geolocalización.
"""
