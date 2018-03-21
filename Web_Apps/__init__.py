
def create_apps(config,application):
    # Create home page
    #my_home_page = create_home(config)
    if application == 'home':
        from .home import create_home
        from .login import create_login
        from .projects import create_project_app
        my_home_page = create_home(config)
        create_login(config)
        create_project_app(config)
        return my_home_page
    elif application == 'login':
        from .login import create_login
        my_login_page = create_login(config)
        return my_login_page
    elif application == 'projects':
        from .projects import create_project_app
        my_project_page = create_project_app(config)
        return my_project_page