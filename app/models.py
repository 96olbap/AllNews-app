class Articles():
    '''
    Articles class that generates new instances of Articles
    '''
    def __init__(self, author, title, description, url, urltoImage, publishedAt, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urltoImage = urltoImage
        self.publishedAt = publishedAt
        self.content = content

class Sources():
    '''
    Sources class that generates new instances of Sources
    '''
    def __init__(self, id, name, description, url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
