from app import app, db
from flask.ext.restless import APIManager
from user.models import User
from user.serializers import user_after_get_many
from blog.serializers import blog_after_get_many
from feature.models import Feature
from document.models import Document
from blog.models import Blog


# API Creation.
methods = ['GET', 'POST', 'PUT', 'DELETE']

manager = APIManager(app, flask_sqlalchemy_db=db)
user_api = manager.create_api_blueprint(User, app=app, methods=methods,
                                        url_prefix='/api/v1', results_per_page=10,
                                        max_results_per_page=100,
                                        postprocessors={
                                            'GET_MANY':[user_after_get_many]
                                        })

blog_api = manager.create_api_blueprint(Blog, app=app, methods=methods,
                                        url_prefix='/api/v1', results_per_page=10,
                                        max_results_per_page=100,
                                        postprocessors={
                                            'GET_MANY':[blog_after_get_many]
                                        })

feature_api = manager.create_api_blueprint(Feature, app=app, methods=methods,
                                           url_prefix='/api/v1', results_per_page=10,
                                           max_results_per_page=100)

document_api = manager.create_api_blueprint(Document, app=app, methods=methods,
                                            url_prefix='/api/v1', results_per_page=10,
                                            max_results_per_page=100)
