from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


app = Flask(__name__)
app.config.from_object("config.Config")


db.init_app(app)
migrate.init_app(app, db)


from app import models


from app.routes import app_routes
app.register_blueprint(app_routes)
