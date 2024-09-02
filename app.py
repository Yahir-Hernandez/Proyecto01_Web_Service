import os
from flask import Flask, render_template, redirect, url_for, request

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
    ciudad = request.args.get('ciudad')
    destino = request.args.get('destino')
    # Aquí podrías hacer la lógica para obtener información del clima
    # Por ejemplo, pasar los datos a una API o realizar cálculos
    return f"Ciudad de origen: {ciudad}, Ciudad de destino: {destino}"

if __name__ == '__main__':
    app.register_error_handler(404, error_page)
    app.run()
