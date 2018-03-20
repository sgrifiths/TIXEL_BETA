from .home import create_home
from .login import create_login


def create_apps(config):
    # Create home page
    my_home_page = create_home(config)
    my_login_page = create_login(config)
    my_return_app = my_home_page or my_login_page
    return my_return_app
