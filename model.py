import numpy as np
import os
import PIL
import PIL.Image
from app import app
import tensorflow as tf

from tensorflow import keras

# Load Model
model = keras.models.load_model('./flower_classifier_model')


def get_prediction(filename):

    class_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

    img_height = 180
    img_width = 180

    # Set the path to the file
    UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
    filename_path = os.path.join(UPLOAD_FOLDER, filename)

    # Load image
    img = keras.preprocessing.image.load_img(
        filename_path, target_size=(img_height, img_width)
    )

    # Transform image to array
    img_array = keras.preprocessing.image.img_to_array(img)

    # Create a batch
    img_array = tf.expand_dims(img_array, 0)

    # Predict
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    predicted_class = class_names[np.argmax(score)]
    predicted_percent = f'{100 * np.max(score):.2f}'

    prediction_message = f'This image most likely belong to {predicted_class} with a {predicted_percent} percent confidence.'
    print(prediction_message)
    print(f'Result: {predicted_class}, {predicted_percent}')

    return predicted_class, predicted_percent
