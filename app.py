import os
from flask import Flask

PROJECT_DIR = os.path.abspath(os.getcwd())
UPLOAD_FOLDER = os.path.join(PROJECT_DIR, 'uploads')

app = Flask(__name__)
app.secret_key = "secret key 123"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
