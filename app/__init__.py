from flask import Flask
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Acceder a las variables de entorno
nombre_variable = os.getenv('NOMBRE_VARIABLE')
otra_variable = os.getenv('OTRA_VARIABLE')

def create_app():
    app = Flask(__name__)

    # Configuración de la app (opcional)
    app.config.from_pyfile('../config.py')

    # Registrar rutas
    from .routes import main
    app.register_blueprint(main)

    return app


