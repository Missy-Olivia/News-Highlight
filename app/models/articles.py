class Articles:
    '''
    Articles class to define articles objects
    '''
    def __init__(self,id,author,title,description,url,urlToImage,date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.date = date