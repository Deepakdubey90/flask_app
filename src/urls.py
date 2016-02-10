"""
This module bind views with url.
"""
from app import app
from user import views


# urls binding with views.
app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/hello/<name>/', view_func=views.test)
app.add_url_rule('/showServices', view_func=views.showServices)
app.add_url_rule('/about', view_func=views.about)
app.add_url_rule('/logout', view_func=views.logout)
app.add_url_rule('/showPortfolio', view_func=views.showPortfolio)
app.add_url_rule('/signUp', view_func=views.UserSignUp.as_view('signUp'))
app.add_url_rule('/signIn', view_func=views.UserSignIn.as_view('signIn'))
#app.add_url_rule('/signIn', view_func=views.signIn, methods=['GET', 'POST'])
