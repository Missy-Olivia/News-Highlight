from flask import render_template
from app import app
from .request import my_news, get_articles
from .models import news_source
News = news_source.News

@app.route('/')
def index():
    '''
	view root page function that returns the index  page and its data
	'''
    sources = my_news('business')
    sports_sources = my_news('sports')
    tech_sources = my_news('technology')
    entertainment_sources = my_news('entertainment')

    title = "News Highlights"

    return render_template('index.html',title = title, sources = sources,sports_sources = sports_sources,tech_sources = tech_sources,entertainment_sources = entertainment_sources)
