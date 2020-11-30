import unittest
from .models import news_source,articles
News = news_source.News
Articles = articles.Articles

class NewsTest(unittest.TestCase):
    '''
    class to test the behaviour of News class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.breakin_news = News("The New Times","Magic Mikey", "Something is breaking and it's bad!","https://www.wsj.com/articles/in-france-thousands-protest-macrons-effort-to-restrict-images-of-police-11606580450","general", "english", "USA")

    def test_instance(self):
        self.assertTrue(isinstance(self.breakin_news, News))

class ArticlesTest(unittest.TestCase):
    '''
    class to test articles class behaviour
    '''
    def setUp(self):
        '''
        set up method to run before every test
        '''
        self.new_article = Articles("the-wall-street-journal", "Loud Silence", "Somewhere over the rainbow", "something is going down there", "https://www.wsj.com/articles/in-france-thousands-protest-macrons-effort-to-restrict-images-of-police-11606580450","https://images.wsj.net/im-265672/social", "2020-11-28T18:43:00Z")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

if __name__ == '__main__':
    unittest.main()