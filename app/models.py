from . import db,login_manager
from flask_login import UserMixin,current_user
from sqlalchemy.sql import func
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    secure_password = db.Column(db.String(255),nullable = False)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blogs = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='user',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='user',lazy='dynamic')


    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password,password) 
    
    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    post = db.Column(db.Text(), nullable = False)
    comment = db.relationship('Comment',backref='blog',lazy='dynamic')
    upvote = db.relationship('Upvote',backref='blog',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='blog',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    
    def save_p(self):
        db.session.add(self)
        db.session.commit()

        
    def __repr__(self):
        return f'Blog {self.post}'

class Comment:

    all_comments = []

    def __init__(self,author,id,quote,permalink,comment):
        self.author = author
        self.id = id
        self.quote = quote
        self.permalink = permalink
        self.comment = comment


    def save_comment(self):
        Comment.all_comments.append(self)


    @classmethod
    def get_comments(cls,id):

        response = []

        for comment in cls.all_comments:
            if comment.blog_id == id:
                response.append(comment)

        return response

class Subscriber(db.Model):
    __tablename__='subscribers'

    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'


class Quote:
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self,author,id,quote,permalink):
        self.author = author
        self.id = id
        self.quote = quote
        self.permalink = 'http://quotes.stormconsultancy.co.uk/quotes/1'
        