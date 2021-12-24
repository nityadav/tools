import numpy as np
import tensorflow as tf

x = np.random.random((10000, 5))
y = np.random.random((10000, 2))

x2 = np.random.random((2000, 5))
y2 = np.random.random((2000, 2))

inp = tf.keras.layers.Input(shape=(5,))
l1 = tf.keras.layers.Dense(256, activation='sigmoid')(inp)
l1 = tf.keras.layers.Dense(256, activation='sigmoid')(l1)
l1 = tf.keras.layers.Dense(256, activation='sigmoid')(l1)
l1 = tf.keras.layers.Dense(256, activation='sigmoid')(l1)
l1 = tf.keras.layers.Dense(256, activation='sigmoid')(l1)
o = tf.keras.layers.Dense(2, activation='sigmoid')(l1)

model = tf.keras.models.Model(inputs=[inp], outputs=[o])
model.compile(optimizer="Adam", loss="mse")

model.fit(x, y, validation_data=(x2, y2), batch_size=500, epochs=500)
