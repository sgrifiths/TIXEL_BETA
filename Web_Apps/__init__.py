from .home import create_home
from .login import create_login


def create_apps(config):
    # Create home page
    home_page = create_home(config)
    login_page = create_login(config)

    return home_page, login_page
