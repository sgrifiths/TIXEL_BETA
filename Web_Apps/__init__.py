from .home import create_home
from .login import create_login


def create_apps(config):
    # Create home page
    my_home_page = create_home(config)
    return my_home_page
