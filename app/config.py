class Config:
    ARTICLES_API_LINK = 'http://newsapi.org/v2/everything?domains=wsj.com&apiKey={}'
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'



class ProdConfig(Config):

    pass

class DevConfig(Config):
    
    DEBUG = True


