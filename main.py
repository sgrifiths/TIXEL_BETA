# copyright enhancedEPM


import Web_Apps
import config

home = Web_Apps.create_apps(config,'home')
Web_Apps.create_apps(config,'login')
Web_Apps.create_apps(config,'projects')

# This is only used when running locally. When running live, gunicorn runs 
# the application. 
if __name__ == '__main__':
    home.run(debug=True)
    login.run(debug=True)
    project.run(debug=True)
