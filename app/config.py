class Config:
    NEWS_API_LINK = 'http://newsapi.org/v2/everything?domains=wsj.com&apiKey={}'


class ProdConfig(Config):

    pass

class DevConfig(Config):
    
    DEBUG = True


