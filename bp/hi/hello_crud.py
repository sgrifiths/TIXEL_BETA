from flask import Blueprint, render_template


def hello_crud():
    hello_crud = Blueprint('hello_crud', __name__)


# [START list]
@hello_crud.route("/")
def list():
    return render_template("index.html")


# [END list]


@hello_crud.route('/view')
def view():
    return render_template("hello_view.html")
