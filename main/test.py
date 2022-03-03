import numpy as np
from tensorflow import keras
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications import mobilenet_v2
import tensorflow as tf


class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']
def preProcessing(img):
    img = img/255
    return img


def prediction(img):

    model_graph = tf.compat.v1.Graph()
    with model_graph.as_default():
        tf_session = tf.compat.v1.Session()
        with tf_session.as_default():
            model = mobilenet_v2.MobileNetV2(weights='imagenet')
    original = keras.preprocessing.image.load_img(img, target_size=(224, 224), color_mode='rgb')
    numpy_img = keras.preprocessing.image.img_to_array(original)
    image_batch = np.expand_dims(numpy_img, axis=0)
    processed_image = mobilenet_v2.preprocess_input(image_batch.copy())

    with model_graph.as_default():
        with tf_session.as_default():
            predictions = model.predict(processed_image)

    label = decode_predictions(predictions, top=1)
    label = label[0][0]
    return label[1]



    return class_names[y_classes[0]]


