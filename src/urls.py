"""
This module bind views with url.
"""
from app import app, db
from flask.ext.restless import APIManager
from user.views import user_module
from endpoints.api import (
    user_api, blog_api,
    feature_api, document_api
)

# url registration.
app.register_blueprint(user_module) # registering Blueprint

# registering API
app.register_blueprint(user_api)
app.register_blueprint(blog_api)
app.register_blueprint(feature_api)
app.register_blueprint(document_api)
