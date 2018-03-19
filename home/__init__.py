from flask import Flask, Blueprint, render_template


def create_app(config):
    home = Flask(__name__)
    home.config.from_object(config)
    profile = Blueprint('home', __name__, template_folder='templates', static_folder='static')
    home.register_blueprint(profile)

    # @home.route('/')
    # def index():
    #    return
    # redirect(url_for('home.home'))

    @home.route('/home')
    def home():
        return render_template('index.html')

    @home.route('/view')
    def view():
        return render_template('hello_view.html')

    return home
