import os
import urllib.parse
from flask import Flask, render_template, redirect, url_for, request, jsonify

from utils.cacheyEscritura import cargar_cache
from utils.obtenerDatosFINALES import datosCiudad, datosTicket
from utils.predicc import porcentaje

#El usuario debe de instalar Flask

app = Flask(__name__)

# Configurar usando variables de entorno o establecer valores directamente en el código
app.config['ENV'] = os.environ.get('FLASK_ENV', 'development')
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', True)
app.secret_key = 'Yahir'

@app.route('/')
def index():
    #Retorna la pagina principal de index
    return render_template('index.html')

def error_page(error):
    return redirect(url_for('index'))

@app.route('/historial')
def historial():
    return render_template('historial.html')

@app.route('/historial/iatas')
def iatas():
    datos = cargar_cache('utils/cache/TicketsConsultados.json')
    return jsonify(datos)

@app.route('/historial/tickets')
def tickets():
    datos = cargar_cache('utils/cache/ClimasConsultados.json')
    return jsonify(datos)
@app.route('/search', methods=['GET'])
def search():
    try:
        ciudad = request.args.get('ciudad')
        codigo_vuelo = request.args.get('iata')

        # Lógica para el formulario 2 (código de vuelo)
        if codigo_vuelo:
            codigo_vuelo = urllib.parse.unquote(codigo_vuelo).replace(' ', '')
            datos = datosTicket(codigo_vuelo)
            if datos:
                return jsonify(datos)
            else:
                return jsonify(["500", "no cargados 1"])

        # Lógica para el formulario 1 (ciudad origen y destino)
        elif ciudad:
            ciudad = urllib.parse.unquote(ciudad).replace(' ', '')

            # Comprobación del porcentaje de coincidencia
            if int(porcentaje(ciudad)[0][1]) < 70:
                return jsonify(["500", "no cargados fff"])

            #Debes de agregar el nuevo metodo que envia el clima actual de la ciudad
            datos = datosCiudad(ciudad)
            
            if datos:
                return jsonify(datos)
            else:
                return jsonify(["500", "no cargados 2"])

        # Si no se proporcionan ni ciudades ni código de vuelo
        else:
            return jsonify(["500", "no cargados 3"])

    except Exception as e:
        return jsonify(["500", f"{e}"])


if __name__ == '__main__':
    app.register_error_handler(404, error_page)
    app.run(debug=True, host='0.0.0.0')
