from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Extension instances
db = SQLAlchemy()
migrate = Migrate()

# Create app factory
app = Flask(__name__)
app.config.from_object("config.Config")

# Initialize extensions with app
db.init_app(app)
migrate.init_app(app, db)

# Import models (important for migrations)
from app import models

# Register the blueprint for routes
from app.routes import app_routes
app.register_blueprint(app_routes)
