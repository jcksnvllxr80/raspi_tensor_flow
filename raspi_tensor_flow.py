import tensorflow as tf

tf.compat.v1.enable_eager_execution()
hello = tf.constant("Hello, TensorFlow!")
print(hello)
