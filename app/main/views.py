from flask import flash, render_template, redirect, url_for,abort,request
from app.email import mail_message
from app.request import get_quotes
from . import main
from flask_login import login_required,current_user
from app.models import User,Blog,Comment,Subscriber,Upvote,Downvote
from .forms import UpdateProfile,BlogForm,CommentForm
from .. import db,photos

@main.route('/')
def index():
    quotes = get_quotes
    blogs = Blog.query.all()
    return render_template('index.html',quote=quotes, blogs = blogs)

@main.route('/create_new', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        user_id = current_user
        new_blog_object = Blog(post=post,user_id=user_id._get_current_object().id,title=title)
        new_blog_object.save_p()
        return redirect(url_for('main.index'))
        
    return render_template('create_blog.html', form = form)

@main.route('/comment/<int:blog_id>', methods = ['GET','POST'])
@login_required
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,blog_id = blog_id)
        new_comment.save_c()
        return redirect(url_for('.comment', blog_id = blog_id))
    return render_template('comment.html', form =form, blog = blog,all_comments=all_comments)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = current_user._get_current_object().id
    posts = Blog.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts)

@main.route('/user/<name>/updateprofile', methods = ['GET','POST'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_u()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/update.html',form =form)


@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))

@main.route('/like/<int:id>',methods = ['GET','POST'])
@login_required
def like(id):
    blog = blog.query.get(id)
    new_vote = Upvote(user = current_user, blog_id=id)
    new_vote.save()
    return redirect(url_for('main.index',blog_id=id))

@main.route('/dislike/<int:id>',methods = ['GET','POST'])
@login_required
def dislike(id):
    blog = Blog.query.get(id)
    new_downvote = Downvote(user = current_user, blog_id=id)
    new_downvote.save()
    return redirect(url_for('main.index',id = id))


@main.route('/subscribe',methods = ['POST','GET'])
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email = email)
    new_subscriber.save_subscriber()
    mail_message("Subscribed to D-Blog","email/welcome_subscriber",new_subscriber.email,new_subscriber=new_subscriber)
    flash('Sucessfuly subscribed')
    return redirect(url_for('main.index'))

@main.route('/blog/<blog_id>/delete', methods = ['POST'])
@login_required
def delete_post(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    blog.delete()
    flash("You have deleted your Blog succesfully!")
    return redirect(url_for('main.index'))
