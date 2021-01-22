#https://www.tensorflow.org/guide/keras/functional/

#%%

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#%%



inputs = keras.Input(shape=(18,), name="Input")
x = layers.Dense(24, activation='sigmoid')(inputs)
x = layers.Dense(24, activation='sigmoid')(x)
x = layers.Dense(24, activation='sigmoid')(x)
y = layers.Dense(24, activation='sigmoid')(inputs)
y = layers.Dense(24, activation='sigmoid')(y)
y = layers.Dense(24, activation='sigmoid')(y)

z = layers.concatenate([x,y])

outputs = layers.Dense(1,activation='sigmoid', name="Output")(z)





model = keras.Model(inputs=[inputs], outputs=[outputs])

model = keras.Model(inputs, outputs, name="toy_resnet")
model.summary()

keras.utils.plot_model(model, "mini_resnet.png", show_shapes=True)

#%%


