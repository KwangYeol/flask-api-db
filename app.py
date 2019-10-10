from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.update(SQLITE_DB_FILE="./test.db")

    from extensions import sqlite
    sqlite.init_app(app)

    from api.experiments import api_experiment
    app.register_blueprint(api_experiment, url_prefix='/experiment')

    return app

app = create_app()