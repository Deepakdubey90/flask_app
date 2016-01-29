import os
import sys
import waitress

BASE_DIR = os.path.join(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from app import app
waitress.serve(
    app,
    host='0.0.0.0',
    port=os.getenv('PORT'),
    cleanup_interval=os.getenv('CLEANUP_INTERVAL', 20),
    channel_timeout=os.getenv('CHANNEL_TIMEOUT', 20))
