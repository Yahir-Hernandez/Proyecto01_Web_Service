import pytest
import sys
import os

ruta_modulos = os.path.abspath(os.path.join(os.path.dirname(__file__), '/src/modules'))

print(ruta_modulos)

from iatas import iatasC  

def test_iatasC_toluca():
    assert iatasC("Toluca") == "TLC"

def test_iatasC_monterrey():
    assert iatasC("Monterrey") == "MTY"

def test_iatasC_ciudad_de_mexico():
    assert iatasC("Ciudad de México") == "MEX"

def test_iatasC_tampico():
    assert iatasC("Tampico") == "TAM"

def test_iatasC_guadalajara():
    assert iatasC("Guadalajara") == "GDL"

def test_iatasC_ciudad_juarez():
    assert iatasC("Ciudad Juárez") == "CJS"

def test_iatasC_cancun():
    assert iatasC("Cancún") == "CUN"

def test_iatasC_tijuana():
    assert iatasC("Tijuana") == "TIJ"

def test_iatasC_hermosillo():
    assert iatasC("Hermosillo") == "HMO"

def test_iatasC_ciudad_del_carmen():
    assert iatasC("Ciudad del Carmen") == "CME"

def test_iatasC_merida():
    assert iatasC("Mérida") == "MID"

def test_iatasC_chetumal():
    assert iatasC("Chetumal") == "CTM"

def test_iatasC_veracruz():
    assert iatasC("Veracruz") == "VER"

def test_iatasC_oaxaca():
    assert iatasC("Oaxaca") == "OAX"

def test_iatasC_huatulco():
    assert iatasC("Huatulco") == "HUX"

def test_iatasC_puerto_vallarta():
    assert iatasC("Puerto Vallarta") == "PVR"

def test_iatasC_puerto_escondido():
    assert iatasC("Puerto Escondido") == "PXM"

def test_iatasC_acapulco():
    assert iatasC("Acapulco") == "ACA"

def test_iatasC_ixtapa_zihuatanejo():
    assert iatasC("Ixtapa-Zihuatanejo") == "ZIH"

def test_iatasC_aguascalientes():
    assert iatasC("Aguascalientes") == "AGU"

def test_iatasC_villahermosa():
    assert iatasC("Villahermosa") == "VSA"

def test_iatasC_cozumel():
    assert iatasC("Cozumel") == "CZM"

def test_iatasC_chihuahua():
    assert iatasC("Chihuahua") == "CUU"

def test_iatasC_torreon():
    assert iatasC("Torreón") == "TRC"

def test_iatasC_queretaro():
    assert iatasC("Querétaro") == "QRO"

def test_iatasC_guanajuato():
    assert iatasC("Guanajuato") == "BJX"

def test_iatasC_puebla():
    assert iatasC("Puebla") == "PBC"

def test_iatasC_san_luis_potosi():
    assert iatasC("San Luis Potosí") == "SLP"

def test_iatasC_zacatecas():
    assert iatasC("Zacatecas") == "ZCL"

def test_iatasC_lima():
    assert iatasC("Lima") == "LIM"

def test_iatasC_la_habana():
    assert iatasC("La Habana") == "HAV"

def test_iatasC_bogota():
    assert iatasC("Bogotá") == "BOG"

def test_iatasC_miami():
    assert iatasC("Miami") == "MIA"

def test_iatasC_los_angeles():
    assert iatasC("Los Ángeles") == "LAX"

def test_iatasC_nueva_york():
    assert iatasC("Nueva York") == "JFK"

def test_iatasC_mazatlan():
    assert iatasC("Mazatlán") == "MZT"

def test_iatasC_ciudad_de_guatemala():
    assert iatasC("Ciudad de Guatemala") == "GUA"

def test_iatasC_belice():
    assert iatasC("Belice") == "BZE"

def test_iatasC_dallas_fort_worth():
    assert iatasC("Dallas/Fort Worth") == "DFW"

def test_iatasC_chicago():
    assert iatasC("Chicago") == "ORD"

def test_iatasC_phoenix():
    assert iatasC("Phoenix") == "PHX"

def test_iatasC_filadelfia():
    assert iatasC("Filadelfia") == "PHL"

def test_iatasC_charlotte():
    assert iatasC("Charlotte") == "CLT"

def test_iatasC_toronto():
    assert iatasC("Toronto") == "YYZ"

def test_iatasC_houston():
    assert iatasC("Houston") == "IAH"

def test_iatasC_vancouver():
    assert iatasC("Vancouver") == "YVR"

def test_iatasC_paris():
    assert iatasC("París") == "CDG"

def test_iatasC_amsterdam():
    assert iatasC("Ámsterdam") == "AMS"

def test_iatasC_atlanta():
    assert iatasC("Atlanta") == "ATL"

def test_iatasC_ciudad_obregon():
    assert iatasC("Ciudad Obregón") == "CEN"

def test_iatasC_madrid():
    assert iatasC("Madrid") == "MAD"

def test_iatasC_santiago_de_chile():
    assert iatasC("Santiago de Chile") == "SCL"

def test_iatasC_austin():
    assert iatasC("Austin") == "AUS"

def test_iatasC_buenos_aires():
    assert iatasC("Buenos Aires") == "EZE"

def test_iatasC_boston():
    assert iatasC("Boston") == "BOS"

def test_iatasC_campeche():
    assert iatasC("Campeche") == "CPE"

def test_iatasC_culiacan():
    assert iatasC("Culiacán") == "CUL"

def test_iatasC_denver():
    assert iatasC("Denver") == "DEN"

def test_iatasC_detroit():
    assert iatasC("Detroit") == "DTW"

def test_iatasC_dubai():
    assert iatasC("Dubái") == "DXB"

def test_iatasC_durango():
    assert iatasC("Durango") == "DGO"

def test_iatasC_estambul():
    assert iatasC("Estambul") == "IST"

def test_iatasC_frankfurt():
    assert iatasC("Frankfurt") == "FRA"

def test_iatasC_la_paz():
    assert iatasC("La Paz") == "LAP"

def test_iatasC_las_vegas():
    assert iatasC("Las Vegas") == "LAS"

def test_iatasC_leon_bajio():
    assert iatasC("León/Bajío") == "BJX"

def test_iatasC_los_mochis():
    assert iatasC("Los Mochis") == "LMM"

def test_iatasC_managua():
    assert iatasC("Managua") == "MGA"

def test_iatasC_manzanillo():
    assert iatasC("Manzanillo") == "ZLO"

def test_iatasC_matamoros():
    assert iatasC("Matamoros") == "MAM"

def test_iatasC_medellin():
    assert iatasC("Medellín") == "MDE"

def test_iatasC_mexicali():
    assert iatasC("Mexicali") == "MXL"

def test_iatasC_minatitlan():
    assert iatasC("Minatitlán") == "MTT"

def test_iatasC_minneapolis():
    assert iatasC("Minneapolis") == "MSP"

def test_iatasC_montreal():
    assert iatasC("Montreal") == "YUL"

def test_iatasC_newark():
    assert iatasC("Newark") == "EWR"

def test_iatasC_nuevo_laredo():
    assert iatasC("Nuevo Laredo") == "NLD"

def test_iatasC_oakland():
    assert iatasC("Oakland") == "OAK"

def test_iatasC_orlando():
    assert iatasC("Orlando") == "MCO"

def test_iatasC_panama():
    assert iatasC("Panamá") == "PTY"

def test_iatasC_raleigh():
    assert iatasC("Raleigh") == "RDU"

def test_iatasC_reynosa():
    assert iatasC("Reynosa") == "REX"

def test_iatasC_roma():
    assert iatasC("Roma") == "FCO"

def test_iatasC_san_antonio():
    assert iatasC("San Antonio") == "SAT"

def test_iatasC_san_francisco():
    assert iatasC("San Francisco") == "SFO"

def test_iatasC_san_salvador():
    assert iatasC("San Salvador") == "SAL"

def test_iatasC_salt_lake_city():
    assert iatasC("Salt Lake City") == "SLC"

def test_iatasC_san_jose():
    assert iatasC("San José") == "SJO"

def test_iatasC_sao_paulo():
    assert iatasC("São Paulo") == "GRU"

def test_iatasC_seattle():
    assert iatasC("Seattle") == "SEA"

def test_iatasC_seul():
    assert iatasC("Seúl") == "ICN"

def test_iatasC_shenzhen():
    assert iatasC("Shenzhen") == "SZX"

def test_iatasC_san_jose_del_cabo():
    assert iatasC("San José del Cabo") == "SJD"

def test_iatasC_santo_domingo():
    assert iatasC("Santo Domingo") == "SDQ"

def test_iatasC_tampa():
    assert iatasC("Tampa") == "TPA"

def test_iatasC_tapachula():
    assert iatasC("Tapachula") == "TAP"

def test_iatasC_tepic():
    assert iatasC("Tepic") == "TPQ"

def test_iatasC_tokio():
    assert iatasC("Tokio") == "NRT"

def test_iatasC_tuxtla_gutierrez():
    assert iatasC("Tuxtla Gutiérrez") == "TGZ"

def test_iatasC_washington_dc():
    assert iatasC("Washington D.C.") == "DCA"
