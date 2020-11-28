from app import app
import urllib.request,json
from news import News

# Getting api key
api_key = app.config['News_Api_key']

# Getting the movie base url
base_url = app.config["News_Api_link"]