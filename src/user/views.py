"""
Views module .
"""
from app import app, db, mail
from flask.views import MethodView
from flask import (Flask, render_template, request,
                   json, flash, redirect, url_for, Blueprint)
from flask.ext.login import login_user, logout_user, current_user
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from utils.utility import login_required
from models import User
from flask_mail import Mail, Message
from flask.ext.api import status
from form import SigninForm, SignupForm
from flask.ext.api.renderers import JSONRenderer
from flask.ext.api.decorators import set_renderers


user_module = Blueprint('user', __name__)

# routing configuration.
login_manager = LoginManager()
login_manager.init_app(app)

@user_module.route('/')
def index():
    """
    Displays the index page accessible at '/'
    """
    return render_template('index.html')

@user_module.route('/hello/<name>/')
def test(name):
    """
    Displays the page greats who ever comes to visit it.
    """
    return render_template('hello.html', name=name)

@user_module.route('/showServices')
@login_required
def showServices():
    """
    Display services .
    """
    return render_template('services.html')

@user_module.route('/about')
@login_required
def about():
     """
     Display portfolio.
     """
     return render_template('about.html')

@user_module.route('/showPortfolio')
@login_required
def showPortfolio():
     """
     Display portfolio.
     """
     return render_template('portfolio.html')

@app.errorhandler(404)
def page_not_found(error):
    """
    Display error page if url not matched.
    """
    return render_template('error.html')

@login_manager.user_loader
def user_loader(user_id):
    user = User.query.filter_by(id=user_id)
    if user.count() == 1:
        return user.one()
    return None

@user_module.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.index'))


class UserSignUp(MethodView):
    """
    user registration views.
    """
    def get(self):
        return render_template('signup.html')

    def post(self):
        form = SignupForm(request.form)
        print("form validate", form.validate())
        print("form errors", form.errors)
        if form.validate()==False:
            print("form errors", form.errors)
            return render_template('signup.html', form=form)
        else:
            #import pdb;pdb.set_trace();
            user = User(
                username=form.username.data,
                password=form.password.data,
                firstname=form.firstname.data,
                lastname=form.lastname.data,
                email=form.email.data
            )
            db.session.add(user)
            db.session.commit()
            msg = Message(
                'Hello'+' '+form.firstname.data+' '+form.lastname.data,
                sender='deepak.dubey@vertisinfotech.com',
                recipients=[form.email.data])
            msg.body = 'Thanks for signup , we will get in touch with you soon!!!'
            mail.send(msg)
            user = User.query.all()
            print("users are :: ", user)
            print("@@@@@@@@@@@ redirected to showSignIn part")
            return redirect(url_for('user.index'))


class UserSignIn(MethodView):
    """
    views to make user login.
    """
    def get(self):
        return render_template('signin.html')

    def post(self):
        form = SigninForm(request.form)
        print("value of form.validate:::::", form.validate())
        if form.validate()==False:
            return render_template('signin.html')
        else:
            user = User.query.filter_by(username=form.username.data)
            login_user(user.one())
            flash('Welcome back {0}'.format(form.username.data))
            print("@@@@@@@@@@@@Login successfully!!!!!")
            return redirect(url_for('user.index'))

# regestering classbased views with blue_print user_module
user_module.add_url_rule('/signUp', view_func=UserSignUp.as_view('signUp'))
user_module.add_url_rule('/signIn', view_func=UserSignIn.as_view('signIn'))
