from flask import Flask, render_template, request, redirect, flash
from app import app
from werkzeug.utils import secure_filename
from model import get_prediction
import os

# Check if the index.py file is run directly
# If so, run the application on localhost address
if __name__ == '__main__':
    app.run(host='127.0.0.1', threaded=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':

        # File not in the request
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        # File not selected
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)

        # File uploaded
        if file:
            # Get file name
            filename = secure_filename(file.filename)

            UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']

            # Save picture
            file.save(os.path.join(UPLOAD_FOLDER, filename))

            # Predict
            get_prediction(os.path.join(UPLOAD_FOLDER, filename))
            class_name, accuracy_percent = get_prediction(filename)

            # Send messages to front end template
            flash(class_name)
            flash(accuracy_percent)
            flash(filename)

            return redirect('/')
