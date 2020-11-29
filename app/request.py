from app import app
import urllib.request,json
from .models import news
News = news.News

# Getting api key
api_key = app.config['News_Api_key']

# Getting the movie base url
base_url = app.config["News_Api_link"]

def my_news():
    '''
    fx that gives json response to our news request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = []

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']

        for item in news_results_list:
            source = item.get('source')
            author = item.get('author')
            title = item.get('title')
            description = item.get('description')
            url = item.get('url')
            poster = item.get('urlToImage')

            news_object = News(source,author,title,description,url,poster)
            news_results.append(news_object)

        return movie_results