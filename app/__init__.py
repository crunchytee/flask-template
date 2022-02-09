from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Configuration

db = SQLAlchemy()
migrate = Migrate()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    from app import models
    from .routes import auth
    app.register_blueprint(auth.bp)
    db.init_app(app)
    migrate.init_app(app, db)
    return app