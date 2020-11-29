import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    class to test the behaviour of News class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.breakin_news = News("The New Times","Magic Mikey","Breaking Bad", "Something is breaking and it's bad!","https://www.wsj.com/articles/in-france-thousands-protest-macrons-effort-to-restrict-images-of-police-11606580450","https://images.wsj.net/im-265672/social")

    def test_instance(self):
        self.assertTrue(isinstance(self.breakin_news, News))

if __name__ == '__main__':
    unittest.main()