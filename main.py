# copyright enhancedEPM


import Web_Apps
import config

app = Web_Apps.create_apps(config)

# This is only used when running locally. When running live, gunicorn runs 
# the application. 
if __name__ == '__main__':
    app.run(debug=True)
