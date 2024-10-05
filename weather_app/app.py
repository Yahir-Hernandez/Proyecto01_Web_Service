import json
import os
import urllib.parse
from flask import Flask, render_template, redirect, url_for, request, jsonify

from utils.obtenervuelos import obtenerIATAS
from utils.obtenerDatosFINALES import datosCiudad, datosTicket
from utils.predicc import porcentaje

app = Flask(__name__)

app.config['ENV'] = os.environ.get('FLASK_ENV', 'development')
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', True)
app.secret_key = 'Yahir'

@app.route('/')
def index():
    return render_template('index.html')

"""
    Ruta principal de la aplicación que renderiza la página de inicio.

    Esta función maneja las solicitudes GET a la ruta raíz ('/') y 
    devuelve el template 'index.html'.

    Returns:
        str: El template 'index.html' renderizado.
"""

def error_page(error):
    return redirect(url_for('index'))

"""
    Redirige a la página principal en caso de error.

    Esta función se utiliza para redirigir a los usuarios a la página de 
    inicio en caso de que ocurra un error en otras rutas.

    Args:
        error: Información sobre el error ocurrido.
    
    Returns:
        Response: Redirección a la página de inicio.
"""

@app.route('/historial')
def historial():
    return render_template('historial.html')

"""
    Ruta que renderiza la página de historial.

    Esta función maneja las solicitudes GET a la ruta '/historial' y 
    devuelve el template 'historial.html'.

    Returns:
        str: El template 'historial.html' renderizado.
"""

@app.route('/historial/iatas')
def iatas():
    carpeta_destino= os.path.join(os.path.dirname(__file__), 'utils/cache')
    ruta = os.path.join(carpeta_destino, 'climas_Consultados.json')
    datos = cargarDatos(ruta)
    return jsonify(datos)

"""
    Ruta que devuelve los datos de IATAS consultados en formato JSON.

    Esta función maneja las solicitudes GET a la ruta '/historial/iatas',
    carga los datos de un archivo JSON y los devuelve en formato JSON.

    Returns:
        Response: Datos en formato JSON de los IATAS consultados.
"""

@app.route('/historial/tickets')
def tickets():
    carpeta_destino= os.path.join(os.path.dirname(__file__), 'utils/cache')
    ruta = os.path.join(carpeta_destino, 'tickets_Consultados.json')
    datos = cargarDatos(ruta)
    return jsonify(datos)

"""
    Ruta que devuelve los datos de tickets consultados en formato JSON.

    Esta función maneja las solicitudes GET a la ruta '/historial/tickets',
    carga los datos de un archivo JSON y los devuelve en formato JSON.

    Returns:
        Response: Datos en formato JSON de los tickets consultados.
"""

def cargarDatos(ruta):
    if os.path.exists(ruta):
        with open(ruta, 'r') as archivo:
            datos = json.load(archivo)
            return datos
    return None

"""
    Carga datos de un archivo JSON si existe.

    Esta función verifica si el archivo en la ruta especificada existe y, 
    si es así, carga su contenido y lo devuelve.

    Args:
        ruta (str): Ruta del archivo JSON a cargar.

    Returns:
        dict: Datos cargados desde el archivo JSON, o None si el archivo no existe.
"""

@app.route('/search', methods=['GET'])
def search():
    try:
        ciudad = request.args.get('ciudad')
        codigo_vuelo = request.args.get('iata')

        if codigo_vuelo:
            codigo_vuelo = urllib.parse.unquote(codigo_vuelo).replace(' ', '')
            datos = datosTicket(codigo_vuelo)
            if datos:
                return jsonify(datos)
            else:
                return jsonify(["500", "no cargados 1"])

        elif ciudad:
            ciudad = urllib.parse.unquote(ciudad).replace(' ', '')

            if int(porcentaje(ciudad)[0][1]) < 70:
                return jsonify(["500", "no cargados fff"])

            datos = datosCiudad(ciudad)
            
            if datos:
                return jsonify(datos)
            else:
                return jsonify(["500", "no cargados 2"])

        else:
            return jsonify(["500", "no cargados 3"])

    except Exception as e:
        return jsonify(["500", f"{e}"])
    
"""
    Realiza una búsqueda de información basada en la ciudad o el código IATA.

    Esta función maneja las solicitudes GET a la ruta '/search', 
    obtiene parámetros de búsqueda de la consulta y devuelve 
    los datos correspondientes en formato JSON. 

    Returns:
        Response: Datos en formato JSON relacionados con la ciudad o el código IATA,
                  o un mensaje de error en caso de fallo.
"""

try:
    obtenerIATAS()
except Exception as e:
    print(f"{e}")

if __name__ == '__main__':
    app.register_error_handler(404, error_page)
    app.run(debug=True, host='0.0.0.0')


