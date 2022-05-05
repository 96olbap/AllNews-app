import unittest
from app import models

Articles = models.Articles

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''
    
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_article = Articles('Alvin Wanjala','Journey of a Programmer','mini description','www.wepukhulu\'s blog','https/imagelink','2022/05/05', 'Media caption')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))


if __name__ == '__main__':
    unittest.main()