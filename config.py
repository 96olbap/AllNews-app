import os
from instance.config import NEWS_API_KEY,SECRET_KEY

class Config:
    
    '''
    General configuration parent class
    '''
    
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SOURCES_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
   




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}