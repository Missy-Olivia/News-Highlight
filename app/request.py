from app import app
import urllib.request,json
from datetime import datetime
from .models import news_source
News = news_source.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_SOURCES_BASE_URL"]

# Getting the articles url
articles_url = app.config["ARTICLES_API_LINK"]

def my_news(category):
    '''
    fx that gives json response to our news source request
    '''
    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = []

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']

        for item in news_results_list:
            id = item.get('id')
            name = item.get('name')
            description = item.get('description')
            url = item.get('url')
            category = item.get('category')
            language = item.get('language')
            country = item.get('country')

            news_object = News(id,name,description,url,category,language,country)
            news_results.append(news_object)

        return news_results

def get_articles(id):
    '''
    function that processes articles and returns article object list
    '''
    get_articles_url = articles_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = []

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']

        for articles_item in articles_results_list:
            id = articles_item.get('id')
            author = articles_item.get('author')
            title = articles_item.get('title')
            description = articles_item.get('description')
            url = articles_item.get('url')
            urlToImage = articles_item.get('urlToImage')
            date = articles_item.get('publishedAt')

            articles_object = Articles(id,author,title,description,url,urlToImage,date)
            articles_results.append(articles_object)

        return articles_results