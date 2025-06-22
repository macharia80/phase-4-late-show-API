# server/app.py

from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import Config
from server import db  # Now this works!

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)  # Initialize db with app
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Import models and routes
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from models.user import User

from controllers.auth_controller import auth_bp
from controllers.guest_controller import guest_bp
from controllers.episode_controller import episode_bp
from controllers.appearance_controller import appearance_bp

app.register_blueprint(auth_bp)
app.register_blueprint(guest_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(appearance_bp)

@app.route('/')
def home():
    return "Late Show API is running!"