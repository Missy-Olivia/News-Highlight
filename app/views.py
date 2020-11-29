from flask import render_template
from app import app
from .request import my_news

@app.route('/')
def index():


    return render_template('index.html')