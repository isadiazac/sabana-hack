from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Registrar rutas
    from .routes import main
    app.register_blueprint(main)

    return app


