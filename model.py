import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf

from tensorflow import keras


model = keras.models.load_model('./flower_classifier_model')

class_names = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']

sunflower_url = 'https://storage.googleapis.com/download.tensorflow.org/example_images/592px-Red_sunflower.jpg'
sunflower_path = tf.keras.utils.get_file('Red_sunflower', origin=sunflower_url)

img_height = 180
img_width = 180
img = keras.preprocessing.image.load_img(
    sunflower_path, target_size=(img_height, img_width)
)

img_array = keras.preprocessing.image.img_to_array(img)
# Create a batch
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

predicted_class = class_names[np.argmax(score)]
predicted_percent = 100 * np.max(score)

print(
    f'This image most likely belong to {predicted_class} with a {predicted_percent:.2f} percent confidence.')
