from flask import Flask, redirect, url_for

from . import authorise
from . import hi


def __init__():
    pass


# def create_app(config, debug=False, testing=False, config_overrides=None):
def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(hi / hello_crud, url_prefix='/index')

    # Register the Auth CRUD blueprint.
    # app.register_blueprint(auth_crud, url_prefix='/auth')

    # Add a default root route.
    @app.route("/")
    def index():
        return redirect(url_for('hello_crud.list'))

    # Add an error handler. This is useful for debugging the live application,
    # however, you should disable the output of the exception for production
    # applications.
    @app.errorhandler(500)
    def server_error(e):
        return """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500

    return app
