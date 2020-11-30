from flask import render_template,redirect,request,url_for
from app import app
from .request import my_news, get_articles
from .models import news_source
News = news_source.News

@app.route('/')
def index():
    '''
	view root page function that returns the index  page and its data
	'''
    business_sources = my_news('business')
    sports_sources = my_news('sports')
    tech_sources = my_news('technology')
    entertainment_sources = my_news('entertainment')

    title = "News Highlights"

    return render_template('index.html',title = title, business_sources = business_sources,sports_sources = sports_sources,tech_sources = tech_sources,entertainment_sources = entertainment_sources)

@app.route('/articles/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles)