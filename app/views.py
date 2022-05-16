from email import message
from random import random
from flask import render_template, redirect, url_for,abort,request
from app import app
from .request import get_quotes,get_quote
from .models import comments
from .forms import CommentForm

Comment=comment.Comment

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting random quotes
    random_quotes = get_quotes('random') 
    title = 'Home - Welcome to Learn Along'
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

@app.route('/quote/<int:id>')
def quote(id):

    '''
    View quote page function that returns the quote details page and its data
    '''
    quote = get_quote(id)
    title = f'{quote.title}'

    return render_template('quote.html',title = title,quote = quote)




# @main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
# @login_required
# def comment(pitch_id):
#     form = CommentForm()
#     pitch = Blog.query.get(pitch_id)
#     all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
#     if form.validate_on_submit():
#         comment = form.comment.data 
#         pitch_id = pitch_id
#         user_id = current_user._get_current_object().id
#         new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
#         new_comment.save_c()
#         return redirect(url_for('.comment', pitch_id = pitch_id))
#     return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)
