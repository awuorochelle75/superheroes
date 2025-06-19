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

# Import routes and models so they are registered with the app
from app import routes, models
