import os
import urllib.parse
from flask import Flask, render_template, redirect, url_for, request, jsonify
from utils.obtenerDatosFINALES import obtenerDatosporCiudad, obtenerDatosporIATA

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

@app.route('/search', methods=['GET'])
def search():
    ciudad_origen = request.args.get('ciudad')
    ciudad_destino = request.args.get('destino')
    codigo_vuelo = request.args.get('iata')

    if codigo_vuelo:
        # Lógica para el formulario 2 (código de vuelo)
        codigo_vuelo = urllib.parse.unquote(codigo_vuelo).replace(' ', '')
        print(codigo_vuelo)
        datos = obtenerDatosporIATA(codigo_vuelo)
        return jsonify(datos)  # Devuelve los datos en formato JSON

    elif ciudad_origen and ciudad_destino:
        # Lógica para el formulario 1 (ciudad origen y destino)
        ciudad_origen = urllib.parse.unquote(ciudad_origen).replace(' ', '')
        ciudad_destino = urllib.parse.unquote(ciudad_destino).replace(' ', '')
        print(ciudad_origen, ciudad_destino)
        datos = obtenerDatosporCiudad(ciudad_origen, ciudad_destino)
        return jsonify(datos)

    else:
        return jsonify([])  # Devuelve una lista vacía en formato JSON


if __name__ == '__main__':
    app.register_error_handler(404, error_page)
    app.run(debug=True)
