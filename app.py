import os
from flask import Flask

PROJECT_DIR = os.path.abspath(os.getcwd())
UPLOAD_FOLDER = os.path.join(PROJECT_DIR, 'static/uploads/')

app = Flask(__name__)
app.secret_key = "secret key 123"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
