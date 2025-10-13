import tensorflow as tf
import sklearn
from tensorflow.python.client import device_lib
print("TensorFlow version:", tf.__version__)
print("Scikit-learn version:", sklearn.__version__)
print(tf.config.list_physical_devices('GPU'))
print(device_lib.list_local_devices())