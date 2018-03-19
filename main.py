# copyright enhancedEPM

import config
import home

app = home.create_app(config)

# This is only used when running locally. When running live, gunicorn runs 
# the application. 
if __name__ == '__main__':
 app.run(debug=True)
