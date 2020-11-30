import os
class Config:
    ARTICLES_API_LINK = 'http://newsapi.org/v2/everything?domains=wsj.com&apiKey={}'
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')




class ProdConfig(Config):

    pass

class DevConfig(Config):
    
    DEBUG = True


