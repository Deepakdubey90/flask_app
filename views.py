from app import app, db, mail
from flask import Flask, render_template, request, json, flash, redirect, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.login import LoginManager
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.sqlalchemy import SQLAlchemy
from models import User
from flask_mail import Mail, Message
from form import SigninForm, SignupForm


@app.route('/signUp',methods=['GET', 'POST'])
def signUp():
    """
    views to make registration.
    """
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        # read the posted values from the UI
        #import pdb; pdb.set_trace();
        form = SignupForm(request.form)
        print("form validate", form.validate())
        print("form errors", form.errors)

        if form.validate()==False:
            print("form errors", form.errors)
            return render_template('signup.html', form=form)
        else:
            import pdb;pdb.set_trace();
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
            return redirect(url_for('index'))
    else:
        return abort(405)

@app.route('/signIn',methods=['GET', 'POST'])
def signIn():
    """
    view to make user login.
    """
    if request.method == 'GET':
        return render_template('signin.html')
    elif request.method == 'POST':
        form = SigninForm(request.form)
        if form.validate==False:
            return render_template('signin.html')
        else:
            user = User.query.filter_by(username=form.username.data)
            login_user(user.one())
            flash('Welcome back {0}'.format(form.username.data))
            print("@@@@@@@@@@@@Login successfully!!!!!")
            return redirect(url_for('index'))
    else:
        return abort(405)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
