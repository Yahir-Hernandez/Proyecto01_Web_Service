import os
import subprocess
import sys
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_project_root():

    return Path(__file__).parent

"""
    Obtiene la ruta del directorio raíz del proyecto.

    Esta función utiliza la ruta del archivo actual (__file__) para 
    determinar y devolver la ruta del directorio que contiene el 
    script en ejecución.

    Returns:
        Path: Ruta del directorio raíz del proyecto.
"""

def create_virtualenv(venv_dir='venv'):

    venv_path = get_project_root() / venv_dir
    if not venv_path.exists():
        logging.info(f"Creando un entorno virtual en {venv_path}...")
        subprocess.check_call([sys.executable, '-m', 'venv', venv_path])
        logging.info(f"Entorno virtual creado en {venv_path}.")
    else:
        logging.info(f"El entorno virtual ya existe en {venv_path}.")

"""
    Crea un entorno virtual en el directorio especificado.

    Esta función verifica si el directorio para el entorno virtual 
    ya existe. Si no existe, crea un nuevo entorno virtual 
    utilizando el módulo 'venv'.

    Args:
        venv_dir (str): Nombre del directorio donde se creará 
                         el entorno virtual. Por defecto es 'venv'.

    Returns:
        None
"""


def install_requirements(venv_dir='venv', requirements_file='requirements.txt'):

    project_root = get_project_root()
    venv_path = project_root / venv_dir
    requirements_path = project_root / requirements_file
    pip_executable = venv_path / 'bin' / 'pip' if sys.platform != 'win32' else venv_path / 'Scripts' / 'pip'

    if not venv_path.exists():
        logging.error(
            f"No se encontró el entorno virtual en {venv_path}. Asegúrate de que el entorno virtual esté creado.")
        return

    if not requirements_path.exists():
        logging.error(f"No se encontró el archivo {requirements_file} en {requirements_path}.")
        return

    try:
        logging.info(f"Instalando paquetes desde {requirements_path}...")
        subprocess.check_call([pip_executable, 'install', '-r', requirements_path])
        logging.info(
            f"Todos los paquetes de {requirements_file} han sido instalados exitosamente en el entorno virtual.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Hubo un error al intentar instalar los paquetes: {e}")
    except Exception as e:
        logging.error(f"Ocurrió un error inesperado: {e}")

"""
    Instala las dependencias listadas en el archivo de requisitos en el entorno virtual.

    Esta función verifica la existencia del entorno virtual y del archivo 
    de requisitos. Si ambos existen, utiliza el ejecutable de pip correspondiente 
    al entorno virtual para instalar los paquetes.

    Args:
        venv_dir (str): Nombre del directorio donde se encuentra el entorno virtual. 
                         Por defecto es 'venv'.
        requirements_file (str): Nombre del archivo que contiene las dependencias 
                                 a instalar. Por defecto es 'requirements.txt'.

    Returns:
        None
"""


def run_app(venv_dir='venv'):

    project_root = get_project_root()
    venv_path = project_root / venv_dir
    python_executable = venv_path / 'bin' / 'python' if sys.platform != 'win32' else venv_path / 'Scripts' / 'python'

    if not venv_path.exists():
        logging.error(
            f"No se encontró el entorno virtual en {venv_path}. Asegúrate de que el entorno virtual esté creado.")
        return

    try:
        logging.info("Ejecutando app.py...")
        os.environ['FLASK_APP'] = 'weather_app/app.py'
        os.environ['FLASK_ENV'] = 'development'  
        os.environ['DEBUG'] = '1'  

        subprocess.check_call([python_executable, '-m', 'flask', 'run'])
        logging.info("app.py se ejecutó exitosamente.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Hubo un error al ejecutar app.py: {e}")
    except Exception as e:
        logging.error(f"Ocurrió un error inesperado: {e}")

"""
    Ejecuta la aplicación Flask desde el entorno virtual.

    Esta función verifica la existencia del entorno virtual, 
    configura las variables de entorno necesarias para ejecutar 
    la aplicación Flask y llama a Flask para iniciar el servidor.

    Args:
        venv_dir (str): Nombre del directorio donde se encuentra el entorno virtual. 
                         Por defecto es 'venv'.

    Returns:
        None
"""


def main():

    create_virtualenv()
    install_requirements()
    run_app()

"""
    Función principal que orquesta la creación del entorno virtual, 
    la instalación de requisitos y la ejecución de la aplicación.

    Esta función crea el entorno virtual, obtiene los IATAS 
    necesarios, instala las dependencias y finalmente 
    ejecuta la aplicación Flask.

    Returns:
        None
"""

if __name__ == '__main__':
    main()