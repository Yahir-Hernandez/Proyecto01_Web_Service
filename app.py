import os
from flask import Flask, render_template, redirect, url_for, request, jsonify
from utils.obtenerDatosFINALES import obtenerDatosporCiudad

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

    if codigo_vuelo != None:
        # Lógica para el formulario 2 (código de vuelo)
        return f"Código de Vuelo recibido:, {codigo_vuelo}\n"
    else:
        datos = obtenerDatosporCiudad(ciudad_origen, ciudad_destino)
        # Lógica para el formulario 1 (ciudad origen y destino)
        return jsonify(datos)

if __name__ == '__main__':
    app.register_error_handler(404, error_page)
    app.run(debug=True)
