from flask import Flask


# def create_app(config, debug=False, testing=False, config_overrides=None):
def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(auth_crud, url_prefix='/login')

    @app.errorhandler(500)
    def server_error(e):
        return """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500

    return app
