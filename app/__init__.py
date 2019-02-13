# import Flask class from flask module
from flask import Flask
from flask_bootstrap import Bootstrap

# create instance of app variable
app = Flask(__name__)

# all other variable instances need to come after the app instances
bootstrap = Bootstrap(app)

# once app variable is created, import the routes to load home page
from app import routes
