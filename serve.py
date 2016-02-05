import os
import sys
import waitress
from app import app

BASE_DIR = os.path.join(os.path.dirname(__file__), 'app')
sys.path.append(BASE_DIR)
waitress.serve(
    app,
    host='0.0.0.0',
    port=os.getenv('PORT'),
    cleanup_interval=os.getenv('CLEANUP_INTERVAL', 20),
    channel_timeout=os.getenv('CHANNEL_TIMEOUT', 20))
