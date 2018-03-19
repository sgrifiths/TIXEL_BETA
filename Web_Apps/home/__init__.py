from flask import Flask, Blueprint, render_template, redirect, url_for


def create_home(config):

    home = Flask(__name__)
    home.config.from_object(config)
    profile = Blueprint('home', __name__, template_folder='templates', static_folder='static')
    home.register_blueprint(profile, url_prefix='/tixel')

    @home.route('/')
    def index():
        return redirect(url_for('my_home'))

    @home.route('/home')
    def my_home():
        return render_template('index.html')

    @home.route('/view')
    def my_view():
        return render_template('hello_view.html')

    @home.route('/list')
    def my_list():
        return render_template('hello_list.html')

    return create_home
