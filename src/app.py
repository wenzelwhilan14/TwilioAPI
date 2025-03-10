from flask import Flask
from src.config.settings import Config
from src.controllers.call_controller import call_bp
from src.controllers.sms_controller import sms_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registrar Blueprints (rutas separadas)
    app.register_blueprint(call_bp, url_prefix="/api/calls")
    app.register_blueprint(sms_bp, url_prefix="/api/sms")

    return app
