from email import message
from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'Hi Sam'
    return render_template('index.html', message = message)

@app.route('/quote/<quote_id>')
def movie(quote_id):

    '''
    View quote page function that returns the quote details page and its data
    '''
    return render_template('quote.html',id = quote_id)
