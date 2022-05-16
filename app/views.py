from email import message
from random import random
from flask import render_template
from app import app
from .request import get_quotes

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting random quotes
    random_quotes = get_quotes('random')
    print(random_quotes)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,random = random_quotes)

@app.route('/quote/<quote_id>')
def movie(quote_id):

    '''
    View quote page function that returns the quote details page and its data
    '''
    return render_template('quote.html',id = quote_id)


def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best learning website online'
    return render_template('index.html', title = title)