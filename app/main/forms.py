from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about yourself.',validators = [InputRequired()])
    submit = SubmitField('Save')

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    blog = TextAreaField('Your Blog', validators=[InputRequired()])
    submit = SubmitField('Blog')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[InputRequired()])
    submit = SubmitField('Comment')