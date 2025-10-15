import tensorflow as tf
import sklearn
from tensorflow.python.client import device_lib
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import matplotlib

print("TensorFlow version:", tf.__version__)
print("Scikit-learn version:", sklearn.__version__)
print(tf.config.list_physical_devices('GPU'))
print(device_lib.list_local_devices())
print("NumPy version:", np.__version__)
print("OpenCV version:", cv2.__version__)
print("Matplotlib version:", matplotlib.__version__)
