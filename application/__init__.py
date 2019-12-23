from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy


def create_app():
    """Initialize the core application"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize plugins
    db.init_app(app)

    with app.app_context():
        # Include routes
        from . import routes

        return app
