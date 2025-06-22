from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.Config')
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    from server.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app