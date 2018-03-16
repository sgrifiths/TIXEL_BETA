from flask import Blueprint, render_template

auth_crud = Blueprint('auth_crud', __name__)


# [START list]
@auth_crud.route("/")
def list():
    return render_template("login.html")


# [END list]


@auth_crud.route('/register')
def view():
    return render_template("register.html")
