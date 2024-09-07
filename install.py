import os
import subprocess
import sys
from pathlib import Path
import logging

# Importar la aplicación Flask desde app.py
from app import app

# Configuración básica del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_project_root():
    """
    Devuelve la ruta del directorio raíz del proyecto.
    """
    return Path(__file__).parent

def create_virtualenv(venv_dir='venv'):
    """
    Crea un entorno virtual en el directorio especificado si no existe.

    :param venv_dir: El directorio en el que se creará el entorno virtual (por defecto 'venv').
    """
    venv_path = get_project_root() / venv_dir
    if not venv_path.exists():
        logging.info(f"Creando un entorno virtual en {venv_path}...")
        subprocess.check_call([sys.executable, '-m', 'venv', venv_path])
        logging.info(f"Entorno virtual creado en {venv_path}.")
    else:
        logging.info(f"El entorno virtual ya existe en {venv_path}.")

def install_requirements(venv_dir='venv', requirements_file='requirements.txt'):
    """
    Instala los paquetes especificados en el archivo requirements.txt en el entorno virtual.

    :param venv_dir: El directorio del entorno virtual (por defecto 'venv').
    :param requirements_file: El archivo que contiene los paquetes a instalar (por defecto 'requirements.txt').
    """
    project_root = get_project_root()
    venv_path = project_root / venv_dir
    requirements_path = project_root / requirements_file
    pip_executable = venv_path / 'bin' / 'pip' if sys.platform != 'win32' else venv_path / 'Scripts' / 'pip'
    
    if not venv_path.exists():
        logging.error(f"No se encontró el entorno virtual en {venv_path}. Asegúrate de que el entorno virtual esté creado.")
        return

    if not requirements_path.exists():
        logging.error(f"No se encontró el archivo {requirements_file} en {requirements_path}.")
        return

    try:
        logging.info(f"Instalando paquetes desde {requirements_path}...")
        subprocess.check_call([pip_executable, 'install', '-r', requirements_path])
        logging.info(f"Todos los paquetes de {requirements_file} han sido instalados exitosamente en el entorno virtual.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Hubo un error al intentar instalar los paquetes: {e}")
    except Exception as e:
        logging.error(f"Ocurrió un error inesperado: {e}")

def run_app():
    """
    Ejecuta la aplicación Flask desde app.py.
    """
    logging.info("Iniciando la aplicación Flask...")
    app.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':
    create_virtualenv()
    install_requirements()
    run_app()
