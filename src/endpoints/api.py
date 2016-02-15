from app import app, db
from flask.ext.restless import APIManager
from user.models import User
from feature.models import Feature
from document.models import Document
from blog.models import Blog


# API Creation.
methods = ['GET', 'POST', 'PUT', 'DELETE']

manager = APIManager(app, flask_sqlalchemy_db=db)
user_api = manager.create_api_blueprint(User, app=app, methods=methods, exclude_columns='password',
                                        url_prefix='/api/v1', results_per_page=10,
                                        max_results_per_page=100)

blog_api = manager.create_api_blueprint(Blog, app=app, methods=methods,
                                        url_prefix='/api/v1', results_per_page=10,
                                        max_results_per_page=100)

feature_api = manager.create_api_blueprint(Feature, app=app, methods=methods,
                                           url_prefix='/api/v1', results_per_page=10,
                                           max_results_per_page=100)

document_api = manager.create_api_blueprint(Document, app=app, methods=methods,
                                            url_prefix='/api/v1', results_per_page=10,
                                            max_results_per_page=100)
