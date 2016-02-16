from functools import wraps
from app import app
from flask import g, request, redirect, url_for
from flask.ext.login import current_user


@app.before_request
def before_request():
    g.user = current_user

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is not None and current_user.is_authenticated:
            return f(*args, **kwargs)
        return redirect(url_for('user.signIn', next=request.url))
    return decorated_function
