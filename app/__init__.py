from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap


#app Initialisation
app = Flask(__name__, instance_relative_config= True)

app.config.from_object(DevConfig)


# Initializing Flask Extensions
bootstrap = Bootstrap(app)

from app import views