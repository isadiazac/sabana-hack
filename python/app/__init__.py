from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuración de la app (opcional)
    app.config.from_pyfile('../config.py')

    # Registrar rutas
    from .routes import main
    app.register_blueprint(main)

    return app