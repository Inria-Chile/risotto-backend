from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import risotto.settings

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(risotto.settings.freeze())

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/health")
    def health():
        return "OK", 200

    @app.cli.command()
    def createdb():
        db.create_all()

    return app
