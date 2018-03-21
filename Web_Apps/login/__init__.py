from flask import Flask, Blueprint, render_template, redirect, url_for

def create_login(config):
    login = Flask(__name__)
    login.config.from_object(config)

    from .login_manager import login_blueprint
    login.register_blueprint(login_blueprint, url_prefix='/login')

    # Add a default root route.
    @login.route("/login")
    def index():
        return redirect(url_for('login_manager.login'))
    return login
