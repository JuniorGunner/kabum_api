from flask import Flask
from blueprints.quote import quote_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(quote_blueprint, url_prefix='/api') # TODO: update with blueprint
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
