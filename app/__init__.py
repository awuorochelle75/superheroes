from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create extension instances
db = SQLAlchemy()
migrate = Migrate()

# Create the app
app = Flask(__name__)
app.config.from_object("config.Config")

# Initialize extensions
db.init_app(app)
migrate.init_app(app, db)

# Import models so migrations can detect them
from app import models

# Register routes blueprint
from app.routes import app_routes
app.register_blueprint(app_routes)
