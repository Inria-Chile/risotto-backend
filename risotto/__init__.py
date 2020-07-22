from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import risotto.settings
from risotto.artifacts import load_artifacts

# db = SQLAlchemy()
# migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(risotto.settings.freeze())

    CORS(app)

    # db.init_app(app)
    # migrate.init_app(app, db)
    load_artifacts(app)

    @app.route("/health")
    def health():
        return "OK", 200

    from risotto.controllers import papers_controller
    from risotto.controllers import topics_controller

    app.register_blueprint(papers_controller.bp)
    app.register_blueprint(topics_controller.bp)

    @app.cli.command()
    def createdb():
        db.create_all()

    return app

