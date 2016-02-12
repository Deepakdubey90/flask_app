"""
This module bind views with url.
"""
from app import app, db
from flask.ext.restless import APIManager
from user.views import user_module
from user.models import User
from feature.models import Feature
from document.models import Document
from blog.models import Blog


# API Creation.
methods = ['GET', 'POST', 'PUT', 'DELETE']

manager = APIManager(app, flask_sqlalchemy_db=db)
user_api = manager.create_api_blueprint(User, app=app, methods=methods,
                                         url_prefix='/api', results_per_page=10,
                                         max_results_per_page=100)

blog_api = manager.create_api_blueprint(Blog, app=app, methods=methods,
                                         url_prefix='/api', results_per_page=10,
                                         max_results_per_page=100)

feature_api = manager.create_api_blueprint(Feature, app=app, methods=methods,
                                         url_prefix='/api', results_per_page=10,
                                         max_results_per_page=100)

document_api = manager.create_api_blueprint(Document, app=app, methods=methods,
                                         url_prefix='/api', results_per_page=10,
                                         max_results_per_page=100)

# url registration.
app.register_blueprint(user_module) # registering Blueprint


# registering API
app.register_blueprint(user_api)
app.register_blueprint(blog_api)
app.register_blueprint(feature_api)
app.register_blueprint(document_api)




'''
# urls binding with views.
app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/hello/<name>/', view_func=views.test)
app.add_url_rule('/showServices', view_func=views.showServices)
app.add_url_rule('/about', view_func=views.about)
app.add_url_rule('/logout', view_func=views.logout)
app.add_url_rule('/showPortfolio', view_func=views.showPortfolio)
#app.add_url_rule('/signUp', view_func=views.UserSignUp.as_view('signUp'))
#app.add_url_rule('/signIn', view_func=views.UserSignIn.as_view('signIn'))
#app.add_url_rule('/signIn', view_func=views.signIn, methods=['GET', 'POST'])
'''
