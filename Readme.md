# Proyecto 01 - Web Service

Repositorio correspondiente al **Proyecto 01 de Modelado y Programación**.

**Profesor:** José Galaviz Casas.

---

## Descripción del Proyecto

Este proyecto consiste en una página web que permite consultar en tiempo real el clima de destinos de vuelo.

El usuario puede realizar consultas mediante:

- La introducción directa de una ciudad.
- El código de un ticket de vuelo que parte o llega al **AICM (Aeropuerto Internacional de la Ciudad de México)**.

---

## Integrantes

| Integrante | Rol |
|---|---|
| Oscar Yahir Hernandez Garcia | Project Manager y desarrollador Front-End |
| Said Apis Lorenzana | Desarrollador Back-End |
| Gerardo Gael Sandoval Sandoval | Beta-Tester y desarrollador de pruebas unitarias |

---

## Tecnologías utilizadas

El proyecto está desarrollado utilizando:

- Python
- JavaScript
- HTML
- CSS

Además, implementa un servicio web utilizando:

- Flask
- APIs externas
- Herramientas adicionales de procesamiento y pruebas

---

# Instalación

Para instalar el proyecto, sigue los siguientes pasos:

## 1. Clonar el repositorio

```bash
git clone https://github.com/PinkFloydFan21/P1_WebService.git
cd P1_WebService/weather_app
```

---

# Configuración previa

Antes de ejecutar el proyecto es necesario configurar las claves de acceso a las APIs utilizadas.

La aplicación requiere:

- Una clave **Hourly Forecast 4 days** de la API de **OpenWeatherMap**.
- Una clave personal de la API de **AviationStack**.

Ambas pueden obtenerse gratuitamente mediante un registro.

> En el caso de OpenWeatherMap, también es necesario presentar una credencial de estudiante.

---

## Configuración de variables de entorno

Una vez obtenidas las claves, dirígete al archivo:

```
<tu_ruta_a_este_proyecto>/weather_app/utils/.env
```

Modifica los valores:

```env
WEATHER_KEY=tu_clave_openweathermap
FLIGHT_KEY=tu_clave_aviationstack
```

Reemplazando los valores por tus respectivas claves.

---

# Ejecución del Proyecto

## Instalación automática de dependencias

Dentro de la carpeta:

```
weather_app/
```

se encuentra el módulo:

```
install.py
```

Este módulo crea un entorno virtual de Python e instala todos los paquetes necesarios.

Ejecuta:

```bash
python3 install.py
```

---

## Paquetes instalados

El instalador configurará las siguientes dependencias:

```
beautifulsoup4==4.12.3
blinker==1.8.2
certifi==2024.8.30
chardet==3.0.4
charset-normalizer==3.3.2
click==8.1.7
deep-translator==1.11.4
Flask==3.0.3
fuzzywuzzy==0.18.0
googletrans==4.0.0rc1
h11==0.9.0
h2==3.2.0
hpack==3.0.0
hstspreload==2024.9.1
httpcore==0.9.1
httpx==0.13.3
hyperframe==5.2.0
idna==2.10
iniconfig==2.0.0
itsdangerous==2.2.0
Jinja2==3.1.4
Levenshtein==0.25.1
MarkupSafe==2.1.5
numpy==2.1.0
packaging==24.1
pandas==2.2.2
pluggy==1.5.0
pytest==8.3.2
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pytz==2024.1
rapidfuzz==3.9.6
requests==2.32.3
rfc3986==1.5.0
six==1.16.0
sniffio==1.3.1
soupsieve==2.6
tzdata==2024.1
urllib3==2.2.2
Werkzeug==3.0.4
```

---

Después de instalar las dependencias:

- Flask se ejecutará automáticamente.
- Se generará el enlace de acceso a la página web.

---

# Prueba de búsqueda mediante tickets

La página permite consultar el clima asociado al origen y destino de vuelos reales.

Para probar esta funcionalidad:

1. Ejecuta el proyecto.
2. Dirígete a:

```
<tu_ruta_a_este_proyecto>/weather_app/utils/cache/
```

3. Abre el archivo:

```
ejemplo_tickets.txt
```

Este archivo contiene tickets recuperados en tiempo real desde la página oficial del **Aeropuerto Internacional de la Ciudad de México**.

---

## Alternativa de prueba

También puedes utilizar cualquier ticket de vuelo real.

Para hacerlo:

1. Ingresa a la página oficial del aeropuerto.
2. Copia un código de vuelo ubicado en la columna de vuelos.
3. Introduce dicho código dentro de la aplicación.

El sistema consultará automáticamente la información del vuelo y mostrará los datos climáticos correspondientes.
