import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils

from tensorflow import keras

# Load Model
model = keras.models.load_model('./flower_classifier_model')


def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image


def get_prediction_content(image):

    class_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

    img_height = 180
    img_width = 180

    # preprocess the image and prepare it for classification
    image = prepare_image(image, target=(img_height, img_width))

    # Predict
    predictions = model.predict(image)
    score = tf.nn.softmax(predictions[0])

    predicted_class = class_names[np.argmax(score)]
    predicted_percent = f'{100 * np.max(score):.2f}'

    prediction_message = f'This image most likely belong to {predicted_class} with a {predicted_percent} percent confidence.'
    print(prediction_message)
    print(f'Result: {predicted_class}, {predicted_percent}')

    return predicted_class, predicted_percent
