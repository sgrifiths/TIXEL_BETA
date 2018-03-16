from flask import Flask


# Register the hello_crud CRUD blueprint.

def __init__():
    from . import hello_crud
    app = Flask(__name__)
    app.register_blueprint(hello_crud, url_prefix='/')

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
