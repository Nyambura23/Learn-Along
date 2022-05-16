import os

class Config:

    QUOTE_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    # QUOTE_API_KEY = os.environ.get('QUOTE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bianca:password@localhost/blog'

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}