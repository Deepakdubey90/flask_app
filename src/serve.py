import os
import sys
import waitress
from app import app


BASE_DIR = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(BASE_DIR)

waitress.serve(
    app,
    host='0.0.0.0',
    port=os.getenv('PORT'))
