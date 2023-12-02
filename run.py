from flask import Flask


def create_app():
    app = Flask(__name__)
    app.register_blueprint(None, url_prefix='/api') # TODO: update with blueprint
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
