from flask import Flask, Blueprint, render_template


def create_login(config):
    login = Flask(__name__)
    login.config.from_object(config)
    login_profile = Blueprint('login', __name__, template_folder='templates', static_folder='static')
    login.register_blueprint(login_profile, url_prefix='/login')

    @login.route('/login')
    def my_login():
        return render_template('login.html')

    @login.route('/login/register')
    def my_register():
        return render_template('register.html')

    @login.route('/login/error')
    def my_error():
        return render_template('error.html')

    return login
